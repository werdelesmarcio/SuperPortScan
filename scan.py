#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import sys
from datetime import datetime
import os
import time


import child

def scan(target,ports):
    for c in ports:
        child(target, c)