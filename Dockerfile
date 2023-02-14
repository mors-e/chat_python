FROM python:3.11-alpine

RUN apk update && apk add --no-cache --virtual gcc python3-dev musl-dev

WORKDIR /chat

COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/sh", "server-entrypoint.sh"]
