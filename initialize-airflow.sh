#!/bin/bash

# Check if the database is already initialized by checking the existence of a marker file
if [ ! -f "/airflow/airflow-init-complete.marker" ]; then
    # Initialize the database
    airflow db init

    # Create a marker file to indicate that initialization is complete
    touch /airflow/airflow-init-complete.marker
fi

# Start the web server in the foreground
exec airflow webserver

