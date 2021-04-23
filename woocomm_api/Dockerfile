FROM python:latest

MAINTAINER diyaneswar.m@msystechnologies.com

RUN mkdir /automation

COPY ./woocomm_api /automation/woocomm_api_test
COPY ./setup.py /automation/

WORKDIR /automation

RUN python3 setup.py  install