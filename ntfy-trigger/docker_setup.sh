#!/bin/bash

handle_error() {
    echo "An error occurred: $1"
}

trap 'handle_error "Something went wrong!"' ERR

#apt install wget
#apt install sed
#apt install docker.io

mkdir /etc/ntfy
cd /etc/ntfy

#wget -O server.yml https://raw.githubusercontent.com/binwiederhier/ntfy/main/server/server.yml
wget -O server.yml https://raw.githubusercontent.com/Su-nlight/mini-projects/main/ntfy-trigger/server.yml


sed -i "14s/.*/base-url: http:\/\/$(hostname -I | awk '{print $1}')/" server.yml
# sed -i "226s/.*/upstream-base-url: \"https://ntfy.sh\" " server.yml

cd ~

# change port number set by me as 2500 to your desired port.

sudo docker run \
-v /var/cache/ntfy:/var/cache/ntfy \
-v /etc/ntfy:/etc/ntfy \
-p 2500:80 \
-itd \
binwiederhier/ntfy \
serve \
--cache-file /var/cache/ntfy/cache.db \
--restart unless-stopped
