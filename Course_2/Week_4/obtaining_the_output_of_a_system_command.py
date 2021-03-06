"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

from os import O_RSYNC
import subprocess

# To be able to process the output of commands, we'll set a parameter called
# 'capture_output' to "true" when calling the run function.
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
# Print and operate with the output generated by the command, which is stored
# in the std out attribute.
print(result.stdout)
# The "B" tells us that this string is not a proper string for Python. It's
# actually an array of bytes. If we want this to become a proper string, we
# can call the decode method. This method applies an encoding to transform
# the bytes into a string. Then we will split it into several pieces.
print(result.stdout.decode().split())

# If we use the capture output parameter and the command writes any output
# to standard error, it will be stored in the 'stderr' attribute of the
# completed process instance.
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

# Check contents of 'stout' and 'stderr' attributes
print(result.stdout)  # Standard output is empty
print(result.stderr)  # But standard error had an output
print(result.stderr.decode())

# This is a great example of how standard output and standard error are
# actually different streams.
