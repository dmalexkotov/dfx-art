export PYTHONPATH=${PYTHONPATH}:/code

python /code/manage.py collectstatic --noinput
python /code/manage.py migrate --noinput

gunicorn dfx_art.wsgi:application --bind 0.0.0.0:8000 --workers 3