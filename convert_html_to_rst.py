"""
Requires
html2rest==0.2.2

1. Recurses through all directories looking for `htm` files, and writes a `rst` version of the file to the same directory.
2. Prints path to created rst file. Pipe this out to create a list of rst files.
"""

import os
from html2rest import html2rest

for dirpath, dirnames, filenames in os.walk("."):
    path=dirpath.split(os.sep)
    for file in filenames:
        current_file = file.split(os.extsep)
        if current_file[1] == "htm":
            # Prints out path for use with content.rst
            print (dirpath+"/"+current_file[0]+".rst")

            # Opens destination file, writes to it, closes destination file.
            write_file = open(os.path.join(dirpath,current_file[0]+'.rst'),"w")
            html2rest(open(os.path.join(dirpath,file)).read(),writer=write_file)
            
            # TODO: 
            # - strip useless information from rst files 
            # e.g. vestigial navigation from templates 
            
            write_file.close()

            # Remove original htm file
            os.remove(os.path.join(dirpath,current_file[0]+"."+current_file[1]))
