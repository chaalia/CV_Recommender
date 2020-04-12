# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/cv_uploader/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev postgresql postgresql-contrib

RUN apk --update add \
    build-base \
    jpeg-dev \
    zlib-dev \
    sudo \
    bash \
    poppler \
    tesseract-ocr

RUN apk add poppler-utils
#RUN chmod g+rx,o+rx /
#RUN adduser -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

# install dependencies
#RUN pip install --upgrade pip
RUN pip install psycopg2-binary
COPY ./requirements.txt /usr/src/cv_uploader/requirements.txt
RUN pip install -r ../requirements.txt

# copy entrypoint.sh
#COPY ./app/entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/cv_uploader
RUN pip3 install nltk
RUN pip3 install spacy
RUN python ../pre_requisites.py

#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
