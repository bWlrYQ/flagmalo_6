FROM debian:latest

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone;

RUN apt-get update && apt-get install -y apache2 \
    cron \
    php \ 
    php-mysql \
    nodejs \
    npm \
    libgbm-dev \
    libasound2 \
    libnss3 \
    nano && \
    apt clean && \
    rm -rf /var/lib/apt/lists/

WORKDIR /var/www/html

COPY ./src ./

RUN chown -R www-data:www-data ./* && \
    rm /var/www/html/index.html;

RUN cd /var/www/html/files/fa6543d2f5258fa531c07f7030a46756/ && npm install puppeteer@18.1.0;

RUN crontab -l | { cat; echo "* * * * * cd /var/www/html/files/fa6543d2f5258fa531c07f7030a46756 && ./toRun.sh >> bot.log"; } | crontab -

RUN chmod +x /var/www/html/files/fa6543d2f5258fa531c07f7030a46756/toRun.sh;

RUN /etc/init.d/cron start;

EXPOSE 80

COPY ./entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh ;

ENV APACHE_RUN_DIR=/var/www/html 
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2.pid
ENV APACHE_RUN_DIR=/var/run/apache2

CMD ["/entrypoint.sh"]
