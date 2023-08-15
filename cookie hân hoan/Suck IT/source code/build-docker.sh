#!/bin/bash
chal="${CHAL:-arenas2-web-suck-it-ver2}"
docker rm -f "$chal"
docker build --tag="$chal" .
docker run -p 1337:1337 --rm --name="${chal}" "${chal}"