FROM ubuntu:latest
RUN apt-get update && apt-get install curl
ADD . /app
RUN cd /app && pip install -r requirements.txt
USER root
