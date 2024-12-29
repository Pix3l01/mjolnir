FROM python:3.13-slim

# Install dependencies
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app
COPY src .

# Run the application
CMD ["python", "bot.py"]
