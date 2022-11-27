FROM php:7.2-apache

RUN apt update && \
    apt install -y python3 && \
    rm -rf /var/lib/apt/lists/*;

COPY src/ /var/www/html/

COPY entrypoint.sh /

ENV FLAG="FMCTF{D0n't_Trust_Us3r_D@ta....}"

RUN chmod +x /entrypoint.sh;

RUN chown root:root /entrypoint.sh
RUN chmod o-r /entrypoint.sh

EXPOSE 80

CMD ["/entrypoint.sh"]
