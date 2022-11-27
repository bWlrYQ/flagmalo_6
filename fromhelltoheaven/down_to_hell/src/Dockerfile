FROM debian:latest

RUN addgroup --gid 1337 flagmalo && \
    useradd -u 1000 --create-home downtohell && \
    echo "downtohell:$(head -c 32 /dev/urandom | base64)" | chpasswd && \
    useradd -u 1001 -G flagmalo --create-home matthieu  && \
    echo "matthieu:$(head -c 32 /dev/urandom | base64)" | chpasswd && \
    useradd -u 1002 -G flagmalo --create-home maxence && \
    echo "maxence:$(head -c 32 /dev/urandom | base64)" | chpasswd && \
    apt-get update && apt-get install -y python3 \
    openssh-client \
    nano \
    python3-distutils \
    curl \
    wget \
    netcat && \
    apt clean && \
    rm -rf /var/lib/apt/lists/ && \

    chmod 750 /home/* && \
    mkdir /bak;

COPY ./privesc1_ssh_key /bak

RUN chown -R matthieu:flagmalo /bak;

WORKDIR /home/downtohell/

COPY ./src .

RUN	wget https://bootstrap.pypa.io/get-pip.py && \
	python3 get-pip.py && \
	pip install django jinja2 flask

RUN chown -R downtohell:downtohell ./

RUN chmod 1773 /tmp;

RUN chown root:root /home/downtohell;

RUN chmod -R 755 /home/downtohell;

RUN chown root:downtohell /home/downtohell/flag.txt && chmod 444 /home/downtohell/flag.txt

USER 1000:1000

CMD ["/usr/bin/python3", "/home/downtohell/app.py"]

