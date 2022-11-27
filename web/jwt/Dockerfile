FROM debian:latest

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone;

RUN apt-get update && apt-get install -y apache2 \
    php \ 
    php-mysql \
    nano && \
    apt clean && \
    rm -rf /var/lib/apt/lists/

WORKDIR /var/www/html

COPY ./src ./

RUN chown -R www-data:www-data ./* && \
    rm /var/www/html/index.html;

EXPOSE 80

ENV APACHE_RUN_DIR=/var/www/html 
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2.pid
ENV APACHE_RUN_DIR=/var/run/apache2

CMD ["apache2","-D", "FOREGROUND"]