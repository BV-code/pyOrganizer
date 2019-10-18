#! /usr/bin/env python3
# a program that searches for a single file extension in the cwd and every sub-directory
# and copies them to a new destination, then sending the original file to the trash
# usage example - pythonOrganizer.py .pdf destination/directory/



import os, shutil, sys, send2trash


for folderName, subfolders, filenames in os.walk('.'):

    for filename in filenames:              
        if filename.endswith(sys.argv[1]):      
            shutil.copy(os.path.join(folderName, filename), sys.argv[2])    # copies the file to the new destination
            print(filename + ' copied to ' + sys.argv[2])
            print(filename + ' sent to trash')
        
            send2trash.send2trash(os.path.join(folderName, filename))	# sends the file to the recycling bin
       
        
        
print('Done')
