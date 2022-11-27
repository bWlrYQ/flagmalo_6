FROM python:3.7.15-alpine3.15

WORKDIR /usr/src/app

RUN pip install --no-cache-dir asyncio

COPY ./src .

CMD [ "python", "./app.py" ]