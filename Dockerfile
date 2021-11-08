FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y libpq-dev \
  && apt-get install -y libzbar-dev \
  && apt-get install -y apt-utils \
  && apt-get install -y gettext \
  && apt-get install -y python3-dev

# Updating pip to latest version
RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY ./start.gunicorn.sh /start-gunicorn
RUN sed -i 's/\r$//g' /start-gunicorn
RUN chmod +x /start-gunicorn

ADD . /app/

WORKDIR /app
