FROM python:3

RUN apt-get update

WORKDIR /app

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

EXPOSE 8000