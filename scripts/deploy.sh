#!/bin/bash
TAG=$1

docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d

docker exec backend python migrate.py

curl -f http://localhost/health || exit 1
