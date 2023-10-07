#!/usr/bin/env bash

export SECRET_KEY="django-insecure-TEST"

export EMAIL_HOST_USER=example@mail.com
export EMAIL_HOST_PASSWORD=mailpassword

export API_KEY=STRIPE_API_KEY
export API_URL=https://api.stripe.com/

export CELERY_BROKER_URL='redis://unused:6379'
export CELERY_RESULT_BACKEND='redis://unused:6379'
export CELERY_TIMEZONE="Europe/Moscow"

export POSTGRES_DB="unused"
export POSTGRES_HOST="unused"
export POSTGRES_USER="unused"
export POSTGRES_PASSWORD=unused
./manage.py test
