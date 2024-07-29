#!/bin/bash
aku=$0
cd
REPOSC="https://raw.githubusercontent.com/genome96/lastone/main"
wget -q "${REPOSC}/menu/menu.zip"
unzip menu.zip
chmod +x menu/*
mv menu/* /usr/local/sbin/
mv menu.zip /etc/alawivpn/menu.zip
rm -rf menu
wget -q -O /etc/xray/versisc "${REPOSC}/versi"
rm -rf ${aku}
rm -rf *${aku}*
