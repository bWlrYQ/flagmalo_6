FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install socat -y
RUN mkdir /ctf
RUN useradd chall
RUN chown -R chall:chall /ctf
WORKDIR /ctf
COPY ./src .
COPY ./entry.sh .
USER chall
EXPOSE 11337
ENTRYPOINT ["/bin/bash", "/ctf/entry.sh"]
