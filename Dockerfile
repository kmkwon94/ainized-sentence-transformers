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

COPY . /sentence-transformers
WORKDIR /sentence-transformers
RUN pip3 install -e .

RUN python3 application_semantic_search_open_corpus.py
RUN mkdir -p upload
EXPOSE 80
CMD python3 ./main.py
