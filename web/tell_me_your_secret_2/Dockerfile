FROM python:3.9

WORKDIR /usr/src/app

RUN pip install --no-cache-dir Flask waitress

COPY ./src .

ENV WERKZEUG_DEBUG_PIN=off

CMD [ "python", "./app.py" ]
