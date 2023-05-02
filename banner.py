#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from datetime import datetime
import os
import time


def banner(s, target, ports):
    try:
        s.settimeout(1)
        s.connect((target,ports))
        banner = s.recv(1024).decode().strip()
        assert banner
        return banner
    except:
        return 'Unknown'