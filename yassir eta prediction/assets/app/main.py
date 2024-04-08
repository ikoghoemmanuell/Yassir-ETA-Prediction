from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import uvicorn

# call the app
app = FastAPI(title="API")

# Load the model and scaler
def load_model_and_scaler():
    with open("model.pkl", "rb") as f1, open("scaler.pkl", "rb") as f2:
        return pickle.load(f1), pickle.load(f2)

model, scaler = load_model_and_scaler()

def predict(df, endpoint="simple"):
    # Scaling
    scaled_df = scaler.transform(df)  # Scale the input data using a pre-defined scaler

    # Prediction
    prediction = model.predict_proba(scaled_df)  # Make predictions using a pre-trained model

    highest_proba = prediction.max(axis=1)  # Get the highest probability for each prediction

    # Assign predicted labels based on the highest probabilities
    predicted_labels = ["Patient does not have sepsis" if i == 0 else "Patient has sepsis" for i in highest_proba]
    print(f"Predicted labels: {predicted_labels}")  # Print the predicted labels to the terminal
    print(highest_proba)  # Print the highest probabilities to the terminal

    response = []
    for label, proba in zip(predicted_labels, highest_proba):
        # Create a response for each prediction with the predicted label and probability
        output = {
            "prediction": label,
            "probability of prediction": str(round(proba * 100)) + '%'  # Convert the probability to a percentage
        }
        response.append(output)  # Add the response to the list of responses

    return response  # Return the list of responses


class Patient(BaseModel):
    Blood_Work_R1: int
    Blood_Pressure: int
    Blood_Work_R3: int
    BMI: float
    Blood_Work_R4: float
    Patient_age: int

class Patients(BaseModel):
    all_patients: list[Patient]

    @classmethod
    def return_list_of_dict(cls, patients: "Patients"):
        patient_list = []
        for patient in patients.all_patients: #for each item in all_patients,
            patient_dict = patient.dict() #convert to a dictionary
            patient_list.append(patient_dict) #add it to the empty list called patient_list
        return patient_list
    
# Endpoints
# Root Endpoint
@app.get("/")
def root():
    return {"Welcome to the Sepsis Prediction API! This API provides endpoints for predicting sepsis based on patient data."}    

# Prediction endpoint
@app.post("/predict")
def predict_sepsis(patient: Patient):
    # Make prediction
    data = pd.DataFrame(patient.dict(), index=[0])
    parsed = predict(df=data)
    return {"output": parsed}

# Multiple Prediction Endpoint
@app.post("/predict_multiple")
def predict_sepsis_for_multiple_patients(patients: Patients):
    """Make prediction with the passed data"""
    data = pd.DataFrame(Patients.return_list_of_dict(patients))
    parsed = predict(df=data, endpoint="multi")
    return {"output": parsed}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)