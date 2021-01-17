#!/usr/bin/env python

from multiprocessing import Pool
import multiprocessing
import subprocess
import os

home_dir = os.path.expanduser("~")
src = home_dir + "/data/prod/"
dest = home_dir + "/data/prod_backup/"

if __name__ == "__main__":
    p = Pool(multiprocessing.cpu_count())
    p.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
