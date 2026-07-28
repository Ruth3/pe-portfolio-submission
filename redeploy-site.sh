#!/usr/bin/env bash

set -e

cd /root/pe-portfolio-submission

git fetch origin
git reset --hard origin/main

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build
