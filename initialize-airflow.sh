#!/bin/bash

# Check if the database is already initialized by checking the existence of a marker file
if [ ! -f "/airflow/airflow-init-complete.marker" ]; then
    # Initialize the database
    airflow db init

    # Create a marker file to indicate that initialization is complete
    touch /airflow/airflow-init-complete.marker
fi

# Create Airflow user
airflow users create \
    --username admin \
    --password admin \
    --firstname John \
    --lastname Doe \
    --role Admin \
    --email admin@example.com

# Start the web server in the foreground
exec airflow webserver
exec airflow scheduler


