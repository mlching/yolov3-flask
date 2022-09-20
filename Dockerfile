# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /yolov3-flask

COPY requirements.txt requirements.txt
COPY . .

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y wget
RUN pip3 install -r requirements.txt
RUN wget https://pjreddie.com/media/files/yolov3.weights

# COPY yolov3.weights yolov3.weights
RUN python weights_download.py

COPY . .

ENV PORT 5000

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app