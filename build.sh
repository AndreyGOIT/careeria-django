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
python manage.py shell -c "
import os
from django.contrib.auth import get_user_model
User = get_user_model()

username = os.environ.get('SUPERUSER_USERNAME')
email = os.environ.get('SUPERUSER_EMAIL') 
password = os.environ.get('SUPERUSER_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Superuser {username} created!')
    else:
        print(f'Superuser {username} already exists.')
else:
    print('Superuser variables not set - skipping creation.')
"
