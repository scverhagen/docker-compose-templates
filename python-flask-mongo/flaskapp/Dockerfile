FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 python3-dev python3-setuptools python3-pip python3-numpy build-essential && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

ENV IN_DOCKER Yes
EXPOSE 80

COPY ./requirements.txt /srv/
COPY ./dockerscript.sh /srv/

WORKDIR /srv
RUN pip3 install -r ./requirements.txt
CMD ./dockerscript.sh