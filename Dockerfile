FROM python:alpine3.10

RUN /sbin/apk add --no-cache --virtual .deps gcc musl-dev \
    && /usr/local/bin/pip install --no-cache-dir black==19.10b0 \
    && /sbin/apk del --no-cache .deps \
    && mkdir /code
WORKDIR /code
ENTRYPOINT [ "python3" ]
