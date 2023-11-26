import re
import sys

if len(sys.argv) < 2:
    print('Chua nhap filename!')
else:
    f = sys.argv[1]
    
    pattern = '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'

    res = []

    with open(f, 'r') as file:
        for line in file:
            s = re.findall(pattern, line)
            if len(s) > 0:
                for item in s:
                    print(item)
                    #res.append(item)

    #print(res)
