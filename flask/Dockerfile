FROM python:3.13.1-slim

WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
