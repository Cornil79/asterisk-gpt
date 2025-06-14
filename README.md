# Asterisk 20 Docker Setup

This project builds a simple Asterisk 20 container and a small Python bridge.

## Build

```
./setup.sh
```

`setup.sh` builds both Docker images using the provided Dockerfiles.

## Run

```
docker compose up
```

Asterisk will start in the `asterisk` container. Ensure there is no
"Stasis initialization failed" message in the logs. The bridge container
starts after Asterisk and waits for audio on `/tmp/audio.pipe`.

