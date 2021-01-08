# Practice Quiz: Undoing Things

1. Let's say we've made a mistake in our latest commit to a public branch. Which of the following commands is the best option for fixing our mistake?

    [x] git revert
    [ ] git commit --amend
    [ ] git reset
    [ ] git checkout -- <file>

2. If we want to rollback a commit on a public branch that wasn't the most recent one using the revert command, what must we do?

    [ ] Use the git reset HEAD~2 command instead of revert
    [ ] Use the revert command repeatedly until we've reached the one we want
    [x] use the commit ID at the end of the git revert command
    [ ] Use the git commit --amend command instead

3. What does Git use cryptographic hash keys for?

    [ ] To secure project backups
    [x] To guarantee the consistency of our repository
    [ ] To encrypt passwords
    [ ] To identify commits

4. What does the command git commit --amend do?

    [ ] Start a new branch
    [ ] Create a copy of the previous commit
    [ ] Delete the previous commit
    [x] Overwrite the previous commit

5. How can we easily view the log message and diff output the last commit if we don't know the commit ID?

    [x] git show
    [ ] git identify
    [ ] git log
    [ ] git revert 