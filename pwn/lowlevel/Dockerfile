FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat \
    gcc \
    nasm \
    openssh-server \
    python3 \
    python2 \
    python3-pip \
    wget \
    build-essential \
    gdb \ 
    nano && \
    apt clean && \
    rm -rf /var/lib/apt/lists/;

RUN mkdir /challenge;

WORKDIR /challenge

COPY ./src/lowlevel.s ./

COPY ./src/flag.txt ./

RUN nasm -f elf64 -o lowlevel.o lowlevel.s && ld -o lowlevel lowlevel.o ;

RUN addgroup --gid 1337 read-flag && \
    useradd -u 1000 --shell=/bin/bash --create-home lowlevel && \
    useradd -u 1001 --shell=/bin/bash -G read-flag lowlevel-cracked && \
    echo "lowlevel:lowlevel" | chpasswd && \
    echo "lowlevel-cracked:$(head -c 32 /dev/urandom | base64)" | chpasswd && \
    echo "Le challenge est aussi disponible en remote sur le port 7001" > readme.txt && \
    chown -R lowlevel-cracked:lowlevel-cracked /challenge && \
    chown root:read-flag flag.txt && \
    chown root:root readme.txt && \
    chown root:root lowlevel.s && \
    chmod 440 flag.txt && \
    chmod 444 readme.txt && \
    chmod 444 lowlevel.s && \
    chmod 4555 lowlevel && \
    chmod 755 /challenge;

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod 500 /entrypoint.sh;

USER 1000:1000

RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py -P /tmp && \
    python2 /tmp/get-pip.py && \
    rm /tmp/get-pip.py && \
    python3 -m pip install pwntools && \
    wget -O ~/.gdbinit-gef.py -q https://gef.blah.cat/py && \
    echo source ~/.gdbinit-gef.py >> ~/.gdbinit;

USER root

CMD ["/entrypoint.sh"]
