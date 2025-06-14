FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

# Обновление и установка зависимостей
RUN apt-get update && apt-get install -y --no-install-recommends \
    gnupg wget \
 && wget -O - https://downloads.asterisk.org/pub/keys/asterisk-signing-key.asc | gpg --dearmor >/usr/share/keyrings/asterisk-archive-keyring.gpg \
 && echo "deb [signed-by=/usr/share/keyrings/asterisk-archive-keyring.gpg] https://packages.asterisk.org/deb $(lsb_release -cs) main" > /etc/apt/sources.list.d/asterisk.list \
 && apt-get update && apt-get install -y --no-install-recommends \
    asterisk=20.* \
    asterisk-dahdi=20.* \
    asterisk-core-sounds-en=20.* \
    asterisk-moh-opsound-wav=20.* \
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

