FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-index --find-links=packages -r requirements.txt

CMD ["python", "app.py"]