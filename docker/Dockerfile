FROM python:3.7.5

RUN useradd --uid 1001 hector \
    && mkdir /app \
    && chown hector: /app
USER hector
WORKDIR /app
