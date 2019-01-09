FROM ubuntu:18.04

RUN apt-get update -y \
  && apt-get install python3-pip -y \
  && pip3 install pip --upgrade \
  && apt-get clean

COPY ./app /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
