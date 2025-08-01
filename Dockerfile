FROM python:3.10-slim

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Launch Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.headless=true"]
