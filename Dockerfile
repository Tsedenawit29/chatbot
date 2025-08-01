# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY app/ ./app
COPY .env .

# Run chatbot (CLI or Streamlit)
CMD ["python", "app/main.py"]
