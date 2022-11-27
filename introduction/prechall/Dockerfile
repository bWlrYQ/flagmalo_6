FROM alpine:3.15.4

RUN apk update; \
    apk add \
        git \
		python3-dev \
		ffmpeg \
		opus-dev \
		openssl-dev \
		libffi-dev \
		build-base && \
	rm -rf /var/lib/apt/lists/* && \

    adduser -D -u 1000 challenge && \
    echo "challenge:$(head -c 32 /dev/urandom | base64)" | chpasswd;

WORKDIR /usr/app
ADD ./src .

RUN	wget https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py && \
	pip install discord.py

RUN chown -R root:challenge /usr/app/ && \
    chown -R root:challenge /home/ && \
    chmod -R g=rx,o= /usr/app/ && \
    chmod -R g=rx,o= /home/

USER 1000:1000

CMD ["/usr/bin/python3", "/usr/app/run.py"]