FROM python:3.12-alpine

COPY app/ /app

WORKDIR /app

CMD ["python", "hello.py"]