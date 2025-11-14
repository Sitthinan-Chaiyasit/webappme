#!/bin/sh
set -e

# default PORT if not set by environment
: "${PORT:=8000}"

echo "Starting migrations (if any)..."
python manage.py migrate --noinput || true

echo "Starting Gunicorn on port ${PORT}"
exec gunicorn myproject.wsgi:application --bind 0.0.0.0:${PORT} --workers 3
