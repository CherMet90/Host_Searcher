import os
import ipaddress
import re

class HostInfo:
    def __init__(self, ip, os):
        self.ip = ip
        self.os = os

    def __repr__(self):
        return f"IP: {self.ip}, OS: {self.os}"

# Replace target_subnet with the subnet you want to scan
target_subnet = '10.10.92.12/32'
nmap_command = 'nmap --osscan-limit --scan-delay 40ms -sV -O {}'
network = ipaddress.ip_network(target_subnet)

for ip in network:
    nmap_output = os.popen(nmap_command.format(str(ip))).read()
    if nmap_output:
        os_match = re.search(r"OS: (.*);", nmap_output)
        if os_match:
            os_name = os_match.group(1)
            host_info = HostInfo(str(ip), os_name)
            print(host_info)
