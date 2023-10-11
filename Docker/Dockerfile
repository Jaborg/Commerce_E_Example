# Use the official Airflow image as the base
FROM apache/airflow:latest

# The working directory in the base image is /opt/airflow
WORKDIR /opt/airflow

# Copy your requirements file into the container
COPY ./requirement.txt .

# Use pip to install the dependencies
RUN pip install --no-cache-dir -r requirement.txt