# Practice Quiz: Python Subprocesses

1. What type of object does a run function return?

    [ ] returncode<br>
    [ ] capture_output<br>
    [ ] stdout<br>
    [x] CompletedProcess

2. How can you change the current working directory where a command will be executed?

    [x] Use the cwd parameter.<br>
    [ ] Use the env parameter.<br>
    [ ] Use the capture_output parameter.<br>
    [ ] Use the shell parameter.

3. When a child process is run using the subprocess module, which of the following are true?
(check all that apply)

    [x] The child process is run in a secondary environment.<br>
    [x] The parent process is blocked while the child process finishes.<br>
    [ ] The parent process and child process both run simultaneously.<br>
    [x] Control is returned to the parent process when the child process ends.<br>

4. When using the run command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command?

    [ ] cwd<br>
    [x] capture_output<br>
    [ ] timeout<br>
    [ ] shell

5. What does the copy method of os.environ do?

    [x] Creates a new dictionary of environment variables<br>
    [ ] Runs a second instance of an environment<br>
    [ ] Joins two strings<br>
    [ ] Removes a file from a directory