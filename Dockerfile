FROM python:3.10.13-slim

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements.txt file first to leverage Docker's layer caching
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 for the Flask app to listen on
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

