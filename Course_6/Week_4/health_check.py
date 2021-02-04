#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
from emails import generate_error_report, send_email


def check_cpu_usage():
    """Verify that there's enough unused CPU."""
    usage = psutil.cpu_percent(1)
    # return usage > 80
    return usage < 80


def check_disk_usage(disk):
    """Verify that there's enough free space on disk."""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def check_available_memory():
    """Check available memory in linux-instance (bytes)."""
    available_memory = psutil.virtual_memory().available/(1024*1024)
    return available_memory > 500


def check_localhost():
    """Check localhost is configured on 127.0.0.1."""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'


if check_cpu_usage():
    error_message = "CPU usage is over 80%"
elif not check_disk_usage('/'):
    error_message = "Available disk space is less than 20%"
elif not check_available_memory():
    error_message = "Available memory is less than 500MB"
elif not check_localhost():
    error_message = "localhost cannot be resolved to 127.0.0.1"
else:
    pass

# If an error is reported then send an email.
if __name__ == "__main__":
    try:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(error_message)
        body = "Please check your system and resolve the issue as soon as possible"
        message = generate_error_report(sender, receiver, subject, body)
        send_email(message)
    except NameError:
        pass
