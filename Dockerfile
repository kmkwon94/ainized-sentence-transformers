FROM ubuntu:latest
MAINTAINER KangMin,Kwon "kmkwon94@gmail.com"
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \ 
    python3-dev \ 
    build-essential \ 
    sudo \
    wget \
    vim 

COPY . /ainized-sentence-transformers
WORKDIR /ainized-sentence-transformers
RUN ["python3", "-m", "pip", "install", "-r", "requirements.txt"]

RUN python3 basic_embedding.py
RUN mkdir -p upload
EXPOSE 80
CMD python3 ./main.py
