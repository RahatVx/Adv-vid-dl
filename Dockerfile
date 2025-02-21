FROM python:3.10-slim

# Install MongoDB and system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ffmpeg \
    && wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - \
    && echo "deb http://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list \
    && apt-get update && apt-get install -y mongodb-org \
    && mkdir -p /data/db

# Install Python dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Start MongoDB and Bot
CMD mongod --fork --logpath /var/log/mongodb.log && \
    gunicorn --bind 0.0.0.0:$FLASK_PORT --workers 1 main:flask_app & \
    python -u main.py
