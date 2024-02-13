FROM python:3

RUN apt-get update

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . /app

RUN pip3 install -r requirements.txt

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate


CMD ["gunicorn","CTFFinal.wsgi","--workers","5","--bind","0.0.0.0:8000"]