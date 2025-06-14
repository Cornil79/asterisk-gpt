FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Обновление и установка зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    asterisk \
    asterisk-dahdi \
    asterisk-core-sounds-en \
    asterisk-moh-opsound-wav \
    openssl \
    curl \
    vim \
    iputils-ping \
    net-tools \
    tzdata \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Копируем кастомные конфиги
COPY etc/asterisk /etc/asterisk

# Поддержка ключей DTLS
VOLUME ["/etc/asterisk/keys", "/var/log/asterisk", "/var/spool/asterisk"]

# SIP + HTTP + RTP
EXPOSE 5060/udp 8088/tcp 10000-20000/udp

# Старт в форграунде
CMD ["bash", "-c", "asterisk -f -vvv"]

