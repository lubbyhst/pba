#!/bin/bash

# fail on error
set -e

# create app dir
mkdir -p /opt/pba

# install app
cp ./app.py /opt/pba/app.py

# install service
cp ./power-button-api.service /etc/systemd/system/power-button-api.service
systemctl daemon-reload
systemctl enable power-button-api.service
systemctl start power-button-api.service
systemctl status power-button-api.service
