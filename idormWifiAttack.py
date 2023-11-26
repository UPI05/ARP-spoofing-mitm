import re
import random
import time
import subprocess

def extract_mac_addresses(file_path):
    mac_address_pattern = r'(?:[A-Fa-f0-9]{2}:){5}[A-Fa-f0-9]{2}'

    with open(file_path, 'r') as file:
        content = file.read()

    return re.findall(mac_address_pattern, content)

# parameters
file_path = input('input file:') 
inf = "wlan0"
pingTimeoutW = "0.1" #s
pingC = "10" 
pingIP = "123.30.151.89"
bingo = False

banned_macs = ["B6:64:F8:B7:7A:A4"]

mac_addresses = extract_mac_addresses(file_path)
random.shuffle(mac_addresses)

i = 1

for mac in mac_addresses:
    if mac.upper() in banned_macs:
        continue

    subprocess.run(["sudo", "ifconfig", inf, "down"], check=True)
    try:
        subprocess.run(["sudo", "macchanger", "-m", mac, inf], check=True)
    except Exception as e:
        print("Error: ", e)

    subprocess.run(["sudo", "ifconfig", inf, "up"], check=True)

    proc = subprocess.run(["ping", "-W", pingTimeoutW, "-c", pingC, pingIP], stdout=subprocess.PIPE, text=True)

    print('Step: ', i, '/', len(mac_addresses))
    print('running...', end='')
    print(mac)
    print(proc.stdout)


    # Check the output for the string "100%" (100% packet lost)
    percent = re.findall(r'[0-9]+%', proc.stdout)
    if len(percent) == 0:
        percent = 100
    else:
        percent = int(percent[0][:-1])


    if percent < 100:
        print('============================== BINGO!!! ==================================')
        print(mac)
        #mac = mac + "\n"
        #with open("ans.out", 'a') as file:
            #file.write(mac)

        bingo = True
        break
    
    i += 1

if bingo:
    # ping to stay loged in
    subprocess.run(["ping", pingIP], check=True) 
else:
    print('================================================')
    print('------------------ NOT FOUND -------------------')
