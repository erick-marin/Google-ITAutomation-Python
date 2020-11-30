"""
This script is used for course notes.

Author: Erick Marin
Date: 11/30/2020
"""

import shutil
import psutil

# disk usage
du = shutil.disk_usage("/")
print(du)

print(du.free/du.total * 100)

# cup_percent function recieves a paramter of usage per second intervals and
# returns an average percentage of usage in that interval.
cpuUsage = psutil.cpu_percent(0.5)
print("{}%".format(cpuUsage))
