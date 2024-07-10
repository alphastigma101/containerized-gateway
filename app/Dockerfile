# Stage 1: Build the environment
FROM python:3.9-slim AS build

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install netcat-openbsd and PostgreSQL client
RUN apt-get update && apt-get install -y netcat-openbsd postgresql-client

# Copy the application
COPY . .

# Copy the entrypoint script
#COPY initialize.sh /usr/src/app/initialize.sh

# Make the entrypoint script executable
#RUN chmod +x /usr/src/app/initialize.sh

# Expose the port (if needed)
EXPOSE 8000
# Command to execute the script which will ask the user to make an account
#ENTRYPOINT ["/usr/src/app/initialize.sh"]
# Corrected CMD instruction to run Django server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
