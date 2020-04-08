FROM python:3.6-buster

RUN pip install pipenv

ADD . /app

WORKDIR /app

RUN pipenv install

CMD pipenv run start
