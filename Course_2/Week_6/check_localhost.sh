#!/bin/bash

# This script is used for course notes.
#
# Author: Erick Marin
# Date: 01/01/2020

if grep "127.0.0.1" /etc/hosts; then
    echo "Everthing ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi