from ipaddress import *

net = ip_network('211.48.136.64/255.255.255.224')

for ip in net:
    n = bin(int(str(ip)[-2] + str(ip)[-1]))[2:]

    if n[-2] + n[-1] == '11':
        print(n)#8