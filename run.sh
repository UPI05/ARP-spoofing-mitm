#!/bin/bash

#handle_ctrl_c() {
#    echo "Ctrl+C pressed, handling the signal."
#    exit 1
#}

#trap handle_ctrl_c SIGINT

sudo nmap -sn 172.16.0.0/22 > nmap-new6 && python listip.py nmap-new6 | sudo ./arp2.sh
#&& sudo ettercap -T -i wlan0 -P dns_spoof 

