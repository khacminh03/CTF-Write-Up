FROM node:current-buster-slim

# Install packages
RUN apt-get update \
    && apt-get install -y supervisor redis-server nginx\
    && rm -rf /var/lib/apt/lists/*

RUN rm /etc/nginx/nginx.conf
COPY config/nginx.conf /etc/nginx/nginx.conf
COPY flag.txt /flag.txt

RUN mkdir -p /chall/app /chall/server

WORKDIR /chall/app
COPY app .
RUN chown -R www-data:www-data .
RUN npm install 

WORKDIR /chall/server
COPY server .
RUN chown -R www-data:www-data .
RUN npm install 

COPY config/supervisord.conf /etc/supervisord.conf

EXPOSE 1337

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]