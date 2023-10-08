FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# This command will run when the container starts
CMD ["python", "./script.py"]
