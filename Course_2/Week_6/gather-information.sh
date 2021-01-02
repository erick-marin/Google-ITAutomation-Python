#!/bin/bash

# This script is used for course notes.
#
# Author: Erick Marin
# Date: 01/01/2020

line="-------------------------------------------------------------------------------"
# Use semi-colons to put serveral command on one-line
echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"