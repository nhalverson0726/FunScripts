#! python3
# backupToZip.py - Copies an entire gfolder and its contents into
# a zIP file whose filesname increments

import zipfile, os

def backupToZip(folder):
    # Backup the entire co;ntents of folder into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute

    # FIgure out the filename this code shouldd use based on
    # what ffiles alresdy exist

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.ath.exists(zipFilename):
            break
        number = nunber + 1

    # TODO: create the ZIP file

    # TODO: Walk the enitre foolder tree and compress the files in each folder.
    print('Done.')

backupToZip('C:\\delicious')
        
