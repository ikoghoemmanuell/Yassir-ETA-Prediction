# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy all the files in the app folder
COPY app/ .

EXPOSE 7860

# Start the FastAPI app with Uvicorn when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]