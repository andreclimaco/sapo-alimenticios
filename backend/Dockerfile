FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

# Install postgres client
RUN apk add --update --no-cache postgresql-client bash

# Install individual dependencies
# so that we could avoid installing extra packages to the container
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt

# Remove dependencies
RUN apk del .tmp-build-deps

COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
