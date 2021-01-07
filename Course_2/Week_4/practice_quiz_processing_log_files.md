# Practice Quiz: Processing Log Files

1. You have created a Python script to read a log of users running CRON jobs. The script needs to accept a command line argument for the path to the log file. Which line of code accomplishes this?

    [ ] import sys<br>
    [x] syslog = sys.argv[1]<br>
    [ ] print(line.strip())<br>
    [ ] usernames = {}

2. Which of the following is a data structure that can be used to count how many times a specific error appears in a log?

    [ ] Get<br>
    [x] Dictionary<br>
    [ ] Search<br>
    [ ] Continue

3. Which keyword will return control back to the top of a loop when iterating through logs?

    [x] Continue<br>
    [ ] Get<br>
    [ ] With<br>
    [ ] Search

4. When searching log files using regex, which regex statement will search for the alphanumeric word "IP" followed by one or more digits wrapped in parentheses using a capturing group#?

    [ ] r"IP \(\d+\)$"<br>
    [ ] b"IP \((\w+)\)$"<br>
    [x] r"IP \((\d+)\)$"<br>
    [ ] r"IP \((\D+)\)$"

5. Which of the following are true about parsing log files?
(Select all thatapply.)

    [ ] Load the entire log files into memory.<br>
    [x] You should parse log files line by line.<br>
    [x] It is efficient to ignore lines that don't contain the information we need.<br>
    [x] We have to open() the log files first.