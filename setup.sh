#!/usr/bin/env bash

mkdir -p service

cat << EOF > service/overseer-lights-button.service
[Unit]
Description=Start the Overseer Lights Button service

[Service]
ExecStart=$(pwd)/start.sh

[Install]
WantedBy=default.target
EOF

sudo cp service/* /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable overseer-lights-button.service
