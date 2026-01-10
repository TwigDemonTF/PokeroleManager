FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps
RUN apt-get update && apt-get install -y build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY Api/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy Api folder
COPY Api ./Api

WORKDIR /app
EXPOSE 5000

# Run as module
CMD ["python3", "-m", "Api.main"]
