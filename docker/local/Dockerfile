# syntax=docker/dockerfile:1

FROM python:3.10-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update \
    && apk upgrade

RUN python -m pip install --upgrade pip
COPY requirements/base.txt requirements.txt
RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "application.py", "bot:telegram:start"]
