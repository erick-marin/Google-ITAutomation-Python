#!/bin/bash

# This script is used for course notes.
#
# Author: Erick Marin
# Date: 01/01/2020

n=0
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;