"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

import os
import subprocess


# This script is modifying the contents of the path environment variable by
# adding a directory to it. We then call the myapp command with that modified
# variable. Doing it this way, the command will run in the modified
# environment with the updated value of path.

# Calling the copy method of the OS environ dictionary that contains the
# current environment variables. This creates a new dictionary that we can
# change as needed without modifying the original environment.
my_env = os.environ.copy()

# The change that we're doing in this script is adding one extra directory to
# the path variable. Remember, the path variable indicates where the operating
# system will look for the executable programs. By adding one entry to the
# path, we're telling the OS to look for programs in an additional location.
# To create the new value, we're calling the join method on the OS path
# substring. This joins elements of the list that we're passing with a path
# separator corresponding to the current operating system. So here, we're
# joining /opt/myapp and the old value of the path variable to the path
# separator.
my_env["PATH"] = os.pathsep.join(["opt/myapp/", my_env["PATH"]])

# Call the myapp command, setting the end parameter to the new environment
# that we've just prepared.
result = subprocess.run(["myapp"], env=my_env)
