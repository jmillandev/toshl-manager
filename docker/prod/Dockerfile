# syntax=docker/dockerfile:1

FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN \
    # Create the user
    addgroup --gid $USER_GID $USERNAME \
    && adduser --disabled-password --uid $USER_UID -G $USERNAME $USERNAME \
    # Upgrade system
    && apk update \
    && apk upgrade \
    && python -m pip install --upgrade pip \
    # Required by dependency_injector
    && apk add --no-cache gcc musl-dev

# Install python packages
COPY requirements requirements
RUN python -m pip install -r requirements/prod.txt

# Copy app folder
USER $USERNAME
WORKDIR /app
COPY --chown=$USERNAME:$USERNAME . .

CMD ["python", "application.py", "bot:telegram:start"]
