#!/usr/bin/env python3
"""
This script is used for course notes.

Author: Erick Marin
Date: 11/30/2020
"""

import requests
import socket


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == "127.0.0.1":
        return True
    return False


def check_connectivity():
    request = requests.get("http://www.google.com")
    response = request.status_code
    if response == 200:
        return True
    return False
