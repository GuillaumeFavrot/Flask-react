FROM python:3.10.4

WORKDIR /app

COPY . .

RUN pip3 install -r ./requirements.txt

WORKDIR /app/backend

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]