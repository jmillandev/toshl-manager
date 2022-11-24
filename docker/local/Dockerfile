# syntax=docker/dockerfile:1

FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

WORKDIR /app

RUN \
    # Create the user
    addgroup --gid $USER_GID $USERNAME \
    && adduser --disabled-password --uid $USER_UID -G $USERNAME $USERNAME \
    # Upgrade system
    && apk update \
    && apk upgrade \
    && python -m pip install --upgrade pip \
    # Add sudo support(Maybe we need to install software after connecting).
    && apk add sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

COPY requirements requirements
RUN python -m pip install -r requirements/local.txt

COPY . .

USER $USERNAME

CMD ["python", "application.py", "bot:telegram:start"]
