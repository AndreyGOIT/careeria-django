#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

echo "Starting build process..."

# Modify the requirements.txt to include necessary packages
echo "Installing dependencies..."
pip install -r requirements.txt

# Convert static asset files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Build completed successfully!"
# Create a superuser if it doesn't exist
#python manage.py createsuperuser --no-input
