import socket
import numpy as np
from cStringIO import StringIO
import itertools
import os
import re

class connection:
    def __init__(self, register):
        self.config = register.get("config")
        self.report = register.get("log")
        self.sock = None
        pass

    def create(self, image):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("192.168.1.3", 10000)
        sock.connect(server_address)
        f = StringIO()
        np.savez_compressed(f, frame=image)
        f.seek(0)
        out = f.read()
        sock.sendall(out)
        sock.shutdown(1)
        sock.close()

    def get_ip(self):
        f = os.popen('ifconfig')
        for iface in [' '.join(i) for i in iter(lambda: list(itertools.takewhile(lambda l: not l.isspace(), f)), [])]:
            if re.findall('^(eth|wlan)[0-9]', iface) and re.findall('RUNNING', iface):
                ip = re.findall('(?<=inet\saddr:)[0-9\.]+', iface)
                if ip:
                    return ip[0]
        return False