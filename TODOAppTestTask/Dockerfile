FROM python:3.10.0-alpine

WORKDIR /app

COPY . /app

RUN apk add gcc
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --system
RUN ["chmod", "+x", "./start-dev-backend.sh"]
