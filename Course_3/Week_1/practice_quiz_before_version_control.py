"""
This script is used for course notes.

Author: Erick Marin
Date: 01/07/2020
"""

# Practice Quiz: Before Version Control
#
# 1. Your colleague sent you a patch called fix_names.patch, which fixes a
# config file called fix_names.conf. What command do you need to run to
# apply the patch to the config file?
#
# [ ] diff names.conf fix_names.conf
# [ ] patch fix_names.conf names.conf
# [x] patch fix_names.conf < fix_names.patch
# [ ] diff names.conf_orig names.conf_fixed > fix_names.conf

# 2. You're helping a friend with a bug in a script called fix_permissions.py,
# which fixes the permissions of a bunch of files. To work on the file, you
# make a copy and call it fix_permissions_modified.py. What command do you
# need to run after solving the bug to send the patch to your friend?
#
# [x] diff fix_permissions.py fix_permissions_modified.py > fix_permissions.patch
# [ ] patch fix_permissions.py < fix_permissions_modified.py
# [ ] patch fix_permissions.py > fix_permissions.patch
# [ ] diff fix_permissions.py fix_permissions.diff

# 3. The _____ command highlights the words that changed in a file instead of
# working line by line.
#
# [ ] diff
# [ ] diff -u
# [x] wdiff
# [ ] patch

# 4. How can we choose the return value our script returns when it finishes?
#
# [x] Using the exit command from the sys module
# [ ] Use the patch command
# [ ] Use the diff command
# [ ] Use meld

# 5. In addition to the original files, what else do we need before we can use
# the patch command?
#
# [x] Diff file
# [ ] exit command of the sys module
# [ ] Version control
# [ ] Full copy of the new files
