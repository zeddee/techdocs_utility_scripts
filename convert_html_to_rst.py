"""
Requires Python 2.7.x
html2rest==0.2.2

Recurses through all directories looking for `htm` files, and writes a `rst` version of the file to the same directory.
"""

import os
from html2rest import html2rest

for dirpath, dirnames, filenames in os.walk("."):
    path=dirpath.split(os.sep)
    print (len(path)-1) * '---', os.path.basename(dirpath)
    for file in filenames:
        current_file = file.split(os.extsep)
        if current_file[1] == "htm":
            write_file = open(os.path.join(dirpath,current_file[0]+'.rst'),"w")
            html2rest(open(os.path.join(dirpath,file)).read(),writer=write_file)
            write_file.close()
