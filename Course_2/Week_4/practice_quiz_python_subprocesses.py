"""
This script is used for course notes.

Author: Erick Marin
Date: 12/21/2020
"""

# Practice Quiz: Python Subprocesses
#
# 1. What type of object does a run function return?
#
# [ ] returncode
# [ ] capture_output
# [ ] stdout
# [x] CompletedProcess
#
# 2. How can you change the current working directory where a command will be
# executed?
#
# [x] Use the cwd parameter.
# [ ] Use the env parameter.
# [ ] Use the capture_output parameter.
# [ ] Use the shell parameter.
#
# 3. When a child process is run using the subprocess module, which of the
# following are true? (check all that apply)
#
# [x] The child process is run in a secondary environment.
# [x] The parent process is blocked while the child process finishes.
# [ ] The parent process and child process both run simultaneously.
# [x] Control is returned to the parent process when the child process ends.
#
# 4. When using the run command of the subprocess module, what parameter, when
# set to True, allows us to store the output of a system command?
#
# [ ] cwd
# [x] capture_output
# [ ] timeout
# [ ] shell
#
# 5. What does the copy method of os.environ do?
#
# [x] Creates a new dictionary of environment variables
# [ ] Runs a second instance of an environment
# [ ] Joins two strings
# [ ] Removes a file from a directory
