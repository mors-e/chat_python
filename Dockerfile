FROM python:alpine3.11

RUN apk update && apk add --no-cache --virtual gcc python3-dev musl-dev

WORKDIR /chat

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["/bin/sh", "server-entrypoint.sh"]
