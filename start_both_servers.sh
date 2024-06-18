#!/bin/bash

# Set environment variables
export DJANGO_SETTINGS_MODULE=backend.nw_backend.settings

# Run Wagtail migrations
echo "Running Wagtail migrations..."
# Navigate to the backend directory
cd backend/nw_backend
python manage.py makemigrations
python manage.py migrate

# Start Wagtail server
echo "Starting Wagtail server..."
python manage.py runserver 8000

# Start Next.js server
#echo "Starting Next.js server..."
#cd frontend 
#npm run dev

# Wait for Next.js to start
#wait -n 10
#echo "Next.js server started."

# Wait for user to stop the server
echo "Press Ctrl+C to stop the servers."
wait