#! /usr/bin/env python3
# a program that searches for a single file exntesion and copies all those files to
# a new destination
# usage example - pythonOrganizer.py .pdf destination/directory/



import os, shutil, sys


for folderName, subfolders, filenames in os.walk('.'):

    for filename in filenames:              
        if filename.endswith(sys.argv[1]):      
            shutil.copy(os.path.join(folderName, filename), sys.argv[2])
       
       
        
        
print('Done')