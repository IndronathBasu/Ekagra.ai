# Use lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies required for torch + psycopg2 if needed
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Copy trained model
COPY trained_model ./trained_model

# Expose service port
EXPOSE 8001

# Start FastAPI service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]