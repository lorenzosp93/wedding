#!/bin/bash

cd /app

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server/beat/worker/flower)"
    exit 1
fi

PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
    if [ "$DJANGO_DEBUG" = "true" ]; then
        gunicorn \
            --reload \
            --bind 0.0.0.0:8000 \
            --timeout 120 \
            --workers 2 \
            --log-level DEBUG \
            --access-logfile "-" \
            --error-logfile "-" \
            wedding.wsgi
    else
        gunicorn \
            --bind 0.0.0.0:8000 \
            --timeout 120 \
            --workers 2 \
            --log-level INFO \
            --access-logfile "-" \
            --error-logfile "-" \
            wedding.wsgi
    fi
elif [ "$PROCESS_TYPE" = "beat" ]; then
    celery \
        --app wedding \
        beat \
        --loglevel INFO \
        --scheduler django_celery_beat.schedulers:DatabaseScheduler
elif [ "$PROCESS_TYPE" = "flower" ]; then
    celery \
        --app wedding \
        flower \
        --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}" \
        --loglevel INFO
elif [ "$PROCESS_TYPE" = "worker" ]; then
    celery \
        --app wedding \
        worker \
        --loglevel INFO
fi