#!/bin/bash

# This script is used for course notes.
#
# Author: Erick Marin
# Date: 01/01/2020

for logfile in /var/log/*log; do
    echo "processing: $logfile"
    cut -d" " -f6 $logfile | sort | uniq -c | sort -nr | head -5
done