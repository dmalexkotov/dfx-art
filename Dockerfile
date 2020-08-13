# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

# Установка пакетов в систему
RUN apt update && \
    apt upgrade && \
    pip install --upgrade pip && \
    pip install wheel pipenv

RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

# Установка зависимостей через pipenv
RUN set -ex && pipenv install --deploy --system --dev

# Service scripts
RUN for i in /code/scripts/*; do \
    sed -i 's/\r//' $i; \
    chmod +x $i; \
    done


RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000

ENTRYPOINT ["entrypoint.sh"]

CMD exec gunicorn dfx_art.wsgi:application --bind 0.0.0.0:8000 --workers 3
