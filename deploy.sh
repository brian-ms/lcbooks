#!/bin/bash

# Navigate to the project directory
cd /home3/imperium/lcbooks/public_html

# Pull the latest changes from GitHub
git pull origin main

# Rebuild Docker containers
docker-compose down
docker-compose up -d --build

# Run database migrations
docker-compose run web python manage.py migrate

# Collect static files (if needed)
docker-compose run web python manage.py collectstatic --noinput

# Restart the application (optional, depending on your setup)
docker-compose restart
