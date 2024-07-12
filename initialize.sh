#!/bin/bash

# Initialize our own variables
username="${POSTGRES_USER}"
password="${POSTGRES_PASSWORD}"
database="${POSTGRES_DB}"

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL is ready!"

# Make the database and credentials
export PGPASSWORD=$password
psql -U $username -h db -c "CREATE DATABASE $database;"
psql -U $username -h db -c "CREATE USER $username WITH ENCRYPTED PASSWORD '$password';"
psql -U $username -h db -c "GRANT ALL PRIVILEGES ON DATABASE $database TO $username;"

# Navigate to the app directory
cd app

# Migrate the database
python manage.py migrate

# Start the Django server
python manage.py runserver 0.0.0.0:8000
