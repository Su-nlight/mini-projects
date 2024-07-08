#!/bin/bash

handle_error() {
    echo "An error occurred: $1"
}

trap 'handle_error "Something went wrong!"' ERR

mkdir /etc/ntfy
cd /etc/ntfy

wget -O server.yml https://raw.githubusercontent.com/Su-nlight/mini-projects/main/ntfy-trigger/server.yml


sudo sed -i "14s/.*/base-url: http:\/\/$(hostname -I | awk '{print $1}')/" server.yml

cd ~

apt install docker.io

sudo docker run \
-v /var/cache/ntfy:/var/cache/ntfy \
-v /etc/ntfy:/etc/ntfy \
-p 80:2500 \
-itd \
binwiederhier/ntfy \
serve \
--cache-file /var/cache/ntfy/cache.db

