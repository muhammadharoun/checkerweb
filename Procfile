web: gunicorn project.wsgi
celery: celery -A project worker -l info
celery: celery -A project beat -l info
