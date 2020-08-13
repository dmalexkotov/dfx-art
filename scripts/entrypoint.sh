export PYTHONPATH=${PYTHONPATH}:/code

python /code/manage.py collectstatic --noinput
python /code/manage.py migrate --noinput

echo Run command ${cmd}
exec ${cmd}
