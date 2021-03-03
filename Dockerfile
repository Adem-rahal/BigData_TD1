FROM ubuntu:20.04

ADD . /API/

WORKDIR /API

RUN apt-get update && apt-get install python3-pip -y && pip3 install -r requirements.txt


CMD python3 my_api.py
