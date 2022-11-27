FROM debian:latest

RUN addgroup --gid 1337 flagmalo_admin && \
    addgroup --gid 7331 flagmalo && \
    useradd -u 1000 -G flagmalo --create-home bwlryq  && \
    echo "bwlryq:$(head -c 32 /dev/urandom | base64)" | chpasswd && \
    useradd -u 1001 -G flagmalo_admin --create-home maxence && \
    echo "maxence:$(head -c 32 /dev/urandom | base64)" | chpasswd && \
    apt-get update && apt-get install -y openssh-server \
    nano \
    python3 \
    sudo \
    netcat && \
    apt clean && \
    rm -rf /var/lib/apt/lists/;

RUN mkdir /home/bwlryq/.ssh/;

COPY ./ssh_key/id_rsa.pub.bak /home/bwlryq/.ssh/authorized_keys

RUN chown -R bwlryq:bwlryq /home/bwlryq/.ssh && chmod 644 /home/bwlryq/.ssh/authorized_keys;

COPY ./entrypoint.sh /entrypoint.sh 

RUN chmod +x /entrypoint.sh;

COPY ./flags/flag_ssh.txt /home/bwlryq/flag.txt

RUN chown root:bwlryq /home/bwlryq/flag.txt && chmod 440 /home/bwlryq/flag.txt

RUN echo '%restricted_sudo ALL=(maxence) NOPASSWD: /usr/bin/python3 /home/maxence/scripts/*' > /etc/sudoers && \
    addgroup restricted_sudo && \
    adduser bwlryq restricted_sudo && \
    mkdir /home/maxence/scripts/;

COPY ./flags/flag_sudo.txt /home/maxence/flag.txt

RUN chown root:maxence /home/maxence/flag.txt && chmod 440 /home/maxence/flag.txt

COPY ./privesc2_sudo_python /home/maxence/scripts/

RUN chown -R maxence:maxence /home/maxence/;

RUN chown root:root /home/bwlryq;

RUN chmod 1773 /tmp;

RUN chmod 660 /etc/passwd && \
    chown root:flagmalo_admin /etc/passwd;

COPY ./flags/flag_root.txt /root/flag.txt

CMD ["/entrypoint.sh"]
