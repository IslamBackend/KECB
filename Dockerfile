FROM python:3.12-slim

LABEL authors="mingo"

ENV PYTHONWRITEBYTECODE=1

ENV PYTHONBUFFERED=1

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]


