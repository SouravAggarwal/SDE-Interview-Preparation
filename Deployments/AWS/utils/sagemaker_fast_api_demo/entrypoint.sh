#!/bin/sh

if [ "$1" = "serve" ]; then
    # Start FastAPI with Uvicorn on port 8080
    exec uvicorn app:app --host 0.0.0.0 --port 8080
else
    # Execute any other command
    exec "$@"
fi