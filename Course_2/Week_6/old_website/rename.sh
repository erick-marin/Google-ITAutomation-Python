#!/bin/bash

# This script is used for course notes.
#
# Author: Erick Marin
# Date: 01/01/2020

for file in *.HTM; do
    name=$(basename "$file" .HTM)
    # It's a really good idea to first run it without actually modifying the
    # file system. This will catch any possible bugs that the script might
    # have. So instead of just running it as it is right now, we'll add an
    # echo in front of the MV command. This means that instead of actually
    # renaming, our script we'll print the renaming that it plans to do.
    echo mv "$file" "$name.html"
done