FROM python:3.11-slim

ARG token
ENV VK_TOKEN $token
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
RUN python db/create_db.py

CMD python main.py
