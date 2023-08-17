#!/bin/sh

# Secure entrypoint
chmod 600 /entrypoint.sh

FLAG=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 5 | head -n 1)

cp /flag.txt /flag$FLAG.txt

echo "" > /flag.txt

exec "$@"