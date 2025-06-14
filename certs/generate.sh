#!/bin/bash
mkdir -p ./certs

openssl req -new -x509 -days 3650 -nodes \
  -out ./certs/asterisk.pem \
  -keyout ./certs/asterisk.key \
  -subj "/CN=asterisk"

cp ./certs/asterisk.pem ./certs/asterisk.crt

echo "✅ Сертификаты сгенерированы в ./certs/"
