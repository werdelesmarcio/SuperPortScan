#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import banner
import socket



def child(target, ports):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3)
        if s.connect_ex((target, ports)) == 0:
            print('{}/tcp open'.format(ports), end='|')
            print(banner(s, target, ports))
    except:
        pass