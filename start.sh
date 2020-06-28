# apply the migrations.
python manage.py migrate

# collect staticfiles.
python manage.py collectstatic --no-input

# create an admin user
python manage.py createadmin

# Start gunicorn server at port 8000 and keep an eye for app code changes.
# If changes occur, kill worker and start a new one.
gunicorn --workers=3 \
    --bind 0.0.0.0:8000 \
    --access-logfile '-' \
    --error-logfile '-' \
    --capture-output \
    casa.wsgi:application