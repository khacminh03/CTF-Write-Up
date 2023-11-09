#!/bin/bash
chal="${CHAL:-command-injection-007}"
docker rm -f "$chal"
docker build --tag="$chal" .
docker run -p 1337:1337 --rm --name="${chal}" "${chal}"