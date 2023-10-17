# Use the official Airflow image as the base
FROM apache/airflow:latest

# The working directory in the base image is /opt/airflow
WORKDIR /opt/airflow

# Set the frontend to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

USER root

# Install 'make' and other system dependencies
RUN apt-get update && apt-get install -y make && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow

# Copy your requirements file into the container
COPY ./requirement.txt .

# Use pip to install the Python dependencies
RUN pip install --no-cache-dir -r requirement.txt
RUN make setup