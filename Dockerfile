FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional but recommended for builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app ./app

# Expose port for Fly.io
ENV PORT=8000

# Run the FastAPI app with Uvicorn -- Copilot's version
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Using "sh -c" allows the shell to expand the $PORT variable (Google's Version)
CMD sh -c "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"
