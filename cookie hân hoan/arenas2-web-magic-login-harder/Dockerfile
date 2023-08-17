FROM php:7.4-fpm-alpine
# Get dependencies
RUN apk add nginx supervisor sqlite-dev && \
  docker-php-ext-install pdo pdo_sqlite && \
  adduser -D www

# Configure packages
COPY config/fpm.conf /usr/local/etc/php-fpm.conf
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/nginx.conf /etc/nginx/nginx.conf

EXPOSE 1337
WORKDIR /www

# Copy challenge files
COPY challenge /www

# Copy flag
COPY flag.txt /flag.txt

# Setup permissions
RUN chown -R www:www /www /var/lib/nginx

# Expose the port nginx is listening on
EXPOSE 1337

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

