FROM python:3.8-slim-buster

WORKDIR /app

COPY ./packages /packages
RUN pip install --no-index --find-links=/packages flask redis

COPY . /app

CMD ["python", "app.py"]
