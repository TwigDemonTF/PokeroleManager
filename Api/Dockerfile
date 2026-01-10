# Use Python 3.13 slim image
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only the backend requirements
COPY Api/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY Api/ ./Api/

WORKDIR /app/Api

EXPOSE 5000

CMD ["python", "-m", "Api.main"]
