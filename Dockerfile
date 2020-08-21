# Use an official Python runtime as a parent image
FROM python:3.7-alpine3.9


# Set environment varibles
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

ENV RUNTIME_PACKAGES \
    libev \
    pcre \
    postgresql-dev \
    docker \
    jpeg-dev \
    zlib-dev \
    libressl-dev \
    libffi-dev \
    openssh

ENV BUILD_PACKAGES \
    libev-dev \
    git \
    build-base \
    pcre-dev \
    gcc \
    linux-headers

# Установка пакетов в систему
RUN apk update && \
    apk upgrade && \
    pip install --upgrade pip && \
    pip install wheel pipenv
RUN apk --no-cache add --virtual build-deps $BUILD_PACKAGES && \
    apk --no-cache add $RUNTIME_PACKAGES

RUN pip install gunicorn

# Copy the current directory contents into the container at /code/
COPY . /code/
# Set the working directory to /code/
WORKDIR /code/

# Установка зависимостей через pipenv
RUN set -ex && pipenv install --deploy --system --dev
RUN apk del build-deps

# Service scripts
RUN for i in /code/scripts/*; do \
    sed -i 's/\r//' $i; \
    chmod +x $i; \
    done

ENV PATH=$PATH:/code/scripts/

# RUN useradd wagtail
# RUN chown -R wagtail /code
# USER wagtail

EXPOSE 8000

ENTRYPOINT entrypoint.sh

CMD exec gunicorn dfx_art.wsgi:application --bind 0.0.0.0:8000 --workers 3
