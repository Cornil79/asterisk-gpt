#!/bin/bash
set -e
mkfifo /tmp/audio.pipe || true
docker compose build
docker compose up
