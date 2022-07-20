# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /yolov3-flask

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "main:app"]
