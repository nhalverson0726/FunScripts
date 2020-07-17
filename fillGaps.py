#! [yhton3
#fillGaps.py fills the gaps in a number scheme of files in a folder
import os, re, shutil

path = 'C:\\PythonTestFolder'

numFiles = os.listdir(path)
numRegex = re.compile(r'(\D*)(\d*)(\D*)')

for file in range(len(numFiles)):
    mo = numRegex.search(numFiles[file])
    num = int(mo.group(2))
    if num != file + 1:
        shutil.move(path + '\\' + numFiles[file], path\
            + '\\' + mo.group(1) +\
            str(file +1) + mo.group(3))
newNames = os.listdir(path)
print(newNames)
    
        
