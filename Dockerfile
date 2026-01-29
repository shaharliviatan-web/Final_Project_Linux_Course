FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the CORRECT script
COPY scripts/py_2.py .

# Run the script
CMD ["python3", "py_2.py"]