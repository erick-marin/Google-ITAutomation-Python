#!/bin/bash

> oldFiles.txt

files=$(grep " jane " /home/k/Documents/Devs/Google-ITAutomation-Python/Course_2/Week_6/Module_Review/data/list.txt | cut -d " " -f 3)

for f in $files; do
    if [ -e $HOME$f ]; then
        echo $HOME$f >> oldFiles.txt
    fi
done