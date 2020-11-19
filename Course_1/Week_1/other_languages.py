"""
This script is used for course notes.

Author: Erick Marin
Date: 10/05/2020
"""

# To explore some of the similarities and differences between various
# scripting languages, let's take a look at a simple program that prints the
# words hello world ten times in three different languages, Python, Bash, and
# PowerShell.

# Bash:
#
#   for i in {1...10}: do
# 	  echo Hello, World!
#   done
#
# PowerShell:
#
#   for ($i=1; $i -le 10; $i++) {
#   	Write-Host "Hello, World!"
#   }

# Python:

for i in range(10):
    print("Hello, World!")
