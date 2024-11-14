FROM python:3.8-alpine

COPY ./ /app
RUN apk update && pip install -r /app/requirements.txt --no-cache-dir
RUN pip install -e /app
EXPOSE 8000
CMD [ "gunicorn", "--bind=0.0.0.0:8000", "wsgi:app" ]
