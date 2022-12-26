FROM python:3.7-slim-buster

ENV PYTHONIOENCODING utf-8
ENV TZ="Asia/Tokyo"
ENV LANG=C.UTF-8
ENV LANGUAGE=en_US:en

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    vim \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install autopep8 selenium pyotp
