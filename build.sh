#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

# Modify the requirements.txt to include necessary packages
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
# Create a superuser if it doesn't exist
#python manage.py createsuperuser --no-input