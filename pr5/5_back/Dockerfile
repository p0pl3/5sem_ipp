FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry


COPY ./requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app