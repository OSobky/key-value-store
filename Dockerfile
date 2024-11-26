FROM python:3.12-alpine

COPY app/ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["fastapi", "run", "main.py", "--workers", "4"]