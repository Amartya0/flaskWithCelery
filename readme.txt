. env1/bin/activate 3 terminals

celery -A app.celery worker --loglevel=info

FLASK_APP=app.py flask shell || FLASK_APP=app.py flask run

celery -A app.celery flower --port=5555
