"""
This script is used for course notes.

Author: Erick Marin
Date: 12/14/2020
"""

from os import write
import csv

hosts = [["workstation.local", "192.168.24.46"],
         ["webserver.cloud", "10.2.5.6"]]

with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
