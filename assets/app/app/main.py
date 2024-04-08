from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import uvicorn
import os

# call the app
app = FastAPI(title="API")

# Load the model and scaler
def load_model_and_scaler(model_filename, scaler_filename):
    model_path = os.path.join(os.path.dirname(__file__), model_filename)
    scaler_path = os.path.join(os.path.dirname(__file__), scaler_filename)
    with open(model_path, "rb") as f1, open(scaler_path, "rb") as f2:
        return pickle.load(f1), pickle.load(f2)

# Define the filenames of the model and scaler files
model_filename = 'model.pkl'
scaler_filename = 'scaler.pkl'

# Load the model and scaler
model, scaler = load_model_and_scaler(model_filename, scaler_filename)

# define your predict function
def predict(df, endpoint="simple"):
    # Scaling
    scaled_df = scaler.transform(df)  # Scale the input data using a pre-defined scaler

    # Prediction
    prediction = model.predict(scaled_df)  # Make predictions using a pre-trained XGBoost regressor model

    response = []
    for eta in prediction:
        # Convert NumPy float to Python native float
        eta = float(eta)
        # Create a response for each prediction with the predicted ETA
        output = {
            "predicted_eta": eta
        }
        response.append(output)  # Add the response to the list of responses

    return response  # Return the list of responses


class Trip(BaseModel):
    Origin_lat: float
    Origin_lon: float
    Destination_lat: float
    Destination_lon: float
    Trip_distance: int # Assuming this column represents an integer value
    total_secs: int # Assuming this column represents an integer value
    dewpoint_2m_temperature: float
    maximum_2m_air_temperature: float
    mean_2m_air_temperature: float
    mean_sea_level_pressure: float
    minimum_2m_air_temperature: float
    surface_pressure: float
    total_precipitation: float
    u_component_of_wind_10m: float
    v_component_of_wind_10m: float

class Trips(BaseModel):
    all_trips: list[Trip]

    @classmethod
    def return_list_of_dict(cls, trips: "Trips"):
        trip_list = []
        for trip in trips.all_trips:  # for each item in all_trips
            trip_dict = trip.dict()    # convert to a dictionary
            trip_list.append(trip_dict)  # add it to the empty list called trip_list
        return trip_list

    
# Endpoints
# Root Endpoint
@app.get("/")
def root():
    return {"Welcome to the ETA Prediction API! This API provides endpoints for predicting ETA based on trip data."}    

# Prediction endpoint
@app.post("/predict")
def predict_eta(trip: Trip):
    # Make prediction
    data = pd.DataFrame(trip.dict(), index=[0])
    predicted_eta = predict(df=data)
    return predicted_eta

# Multiple Prediction Endpoint
@app.post("/predict_multiple")
def predict_eta_for_multiple_trips(trips: Trips):
    """Make prediction with the passed data"""
    data = pd.DataFrame(Trips.return_list_of_dict(trips))
    predicted_eta = predict(df=data, endpoint="multi")
    return {"predicted_eta": predicted_eta}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)