web: gunicorn WtfApi.wsgi
worker: celery --app WtfApi worker --beat --loglevel=INFO
