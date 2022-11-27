FROM alpine:3.15.4

# Init
RUN apk update; \
    apk add \
        git \
		python3-dev \
		ffmpeg \
		iputils \
		opus-dev \
		openssl-dev \
		libffi-dev \
		build-base && \
	rm -rf /var/lib/apt/lists/* && \
# Create user
    adduser -D -u 1000 challenge && \
    echo "challenge:$(head -c 32 /dev/urandom | base64)" | chpasswd;

# Copy chall data
WORKDIR /usr/app
ADD ./src .

# Install python packages
RUN	wget https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py && \
	pip install discord.py

# fix permissions
RUN chown -R root:challenge /usr/app/ && \
    chown -R root:challenge /home/ && \
    chmod -R g=rx,o= /usr/app/ && \
    chmod -R g=rx,o= /home/

# Switch user
USER 1000:1000

# Start
CMD ["/usr/bin/python3", "/usr/app/run.py"]