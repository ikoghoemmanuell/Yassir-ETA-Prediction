# yassir-eta-prediction-challenge-for-azubian

[![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/ikoghoemmanuell?tab=repositories)
[![View My Profile](https://img.shields.io/badge/MEDIUM-Article-purple?logo=Medium)](https://github.com/ikoghoemmanuell/Grocery-Store-Forecasting-Challenge-For-Azubian/blob/main/Article.md)
[![Streamlit App](https://img.shields.io/badge/FastAPI-App-yellow)](https://huggingface.co/spaces/ikoghoemmanuell/SEER-A_sales_forecasting_app)
[![Website](https://img.shields.io/badge/My-Website-darkgreen)](https://emmanuelikogho.netlify.app/)
![alt text](image.png)

Predict the estimated time of arrival at the dropoff point for a single Yassir journey.

## Introduction

Ride-hailing apps like Uber and Yassir rely on real-time data and machine learning algorithms to automate their services. Accurately predicting the estimated time of arrival (ETA) for Yassir trips will make Yassir's services more reliable and attractive; this will have a direct and indirect impact on both customers and business partners. The solution would help the company save money and allocate more resources to other parts of the business.

The objective of this project is to predict the estimated time of arrival at the dropoff point for a single Yassir journey.

## Dataset

The dataset used for this case study is provided [here](https://github.com/ikoghoemmanuell/Yassir-ETA-Prediction/tree/main/assets/data).

The data contains details for 119,549 trips (train and test are split by date). Each row contains a start location and end location (reported as latitude and longitude to within approximately 100m) and the travel distance along the fastest route. Each trip also has a timestamp, which can be used to pull the weather for that day from Weather.csv file. The weather data includes temperature, rainfall and wind speed for the time period during which the trip data was collected.

## Setup

Install the required packages to be able to run the evaluation locally.

You need to have [`Python 3`](https://www.python.org/) on your system (**a Python version lower than 3.10**). Then you can clone this repo and being at the repo's `root :: repository_name> ...` follow the steps below:

- Windows:

```python
python -m venv venv; venv\Scripts\activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
```

- Linux & MacOs:

```python
python3 -m venv venv; source venv/bin/activate; python -m pip install -q --upgrade pip; python -m pip install -qr requirements.txt
```

The both long command-lines have a same structure, they pipe multiple commands using the symbol `;` but you may manually execute them one after another.

1. **Create the Python's virtual environment** that isolates the required libraries of the project to avoid conflicts;
2. **Activate the Python's virtual environment** so that the Python kernel & libraries will be those of the isolated environment;
3. **Upgrade Pip, the installed libraries/packages manager** to have the up-to-date version that will work correctly;
4. **Install the required libraries/packages** listed in the `requirements.txt` file so that it will be allow to import them into the python's scripts and notebooks without any issue.

**NB:** For MacOs users, please install `Xcode` if you have an issue.

## Repository Structure

The repository is organized as follows:

- `data/`: Contains the dataset files.
- `notebooks/`: Contains Jupyter notebooks showcasing the step-by-step implementation of the case study, including EDA, feature engineering, model development, and evaluation.
- `dev/`: Contains any source code or scripts used in the case study, such as data preprocessing or custom functions.

Feel free to explore the notebooks and source code to gain a deeper understanding.

## Run FastAPI

To run the fastAPI, paste this code to your terminal:

```python
uvicorn main:app — reload
```

When you run the script and start the web server using Uvicorn, your FastAPI application becomes accessible at

```python
http://127.0.0.1:8000
```

To access the documentation of your API, you can simply add “/docs” to the URL:

```python
http://127.0.0.1:8000/docs
```

## Screenshots

![ezgif com-optimize (1)](https://github.com/ikoghoemmanuell/Machine-Learning-API-using-FastAPI/assets/102419217/a8352c5f-afea-43b1-8bf5-c24607cf3481)
![ezgif com-crop](https://github.com/ikoghoemmanuell/Machine-Learning-API-using-FastAPI/assets/102419217/df0ed5a8-2daf-47ca-a4f5-e6128429d5d3)

## Resources

Here are some ressources you would read to have a good understanding of FastAPI :

- [Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [Video - Building a Machine Learning API in 15 Minutes ](https://youtu.be/C82lT9cWQiA)
- [FastAPI for Machine Learning: Live coding an ML web application](https://www.youtube.com/watch?v=_BZGtifh_gw)
- [Video - Deploy ML models with FastAPI, Docker, and Heroku ](https://www.youtube.com/watch?v=h5wLuVDr0oc)
- [FastAPI Tutorial Series](https://www.youtube.com/watch?v=tKL6wEqbyNs&list=PLShTCj6cbon9gK9AbDSxZbas1F6b6C_Mx)
- [Http status codes](https://www.linkedin.com/feed/update/urn:li:activity:7017027658400063488?utm_source=share&utm_medium=member_desktop)

## 👏 Support

If you found this article helpful, please give it a clap or a star on GitHub!

## Author

- [Emmanuel Ikogho](https://www.linkedin.com/in/emmanuel-ikogho-6b959b24b/)
