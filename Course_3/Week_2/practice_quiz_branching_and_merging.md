# Practice Quiz: Branching & Merging

1. When we merge two branches, one of two algorithms is used. If the branches have diverged, which algorithm is used?

    [x] three-way merge<br>
    [ ] fast-forward merge<br>
    [ ] merge conflict<br>
    [ ] orphan-creating merge

2. The following code snippet represents the result of a merge conflict. Edit the code to fix the conflict and keep the version represented by the current branch.

    ```
    print("Keep me!")
    ```

3. What command would we use to throw away a merge, and start over? 

    [ ] git checkout -b \<branch> <br>
    [X] git merge --abort<br>
    [ ] git log --graph --oneline 
    [ ] git branch -D <name>

4. How do we display a summarized view of the commit history for a repo, showing one line per commit? 

    [ ] git log --format=short 
    [ ] git branch -D <name>
    [x] git log --graph --oneline 
    [ ] git checkout -b <branch>

5. The following script contains the result of a merge conflict. Edit the code to fix the conflict, so that both versions are included.

    ```
    def main():
        print("Start of program>>>>>>>")
        print("End of program!")

    main()
    ```