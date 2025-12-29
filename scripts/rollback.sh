#!/bin/bash
echo "Rolling back..."
docker compose down
docker compose up -d
