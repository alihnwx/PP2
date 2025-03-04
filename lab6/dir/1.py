import os

path = "/Users/alihaan/Desktop/PP2/lab6/dir"
allElements = os.listdir(path)
allDirs, allFiles = [], []
for el in allElements:
    if os.path.isdir(os.path.join(path, el)):
        allDirs.append(el)

for el in allElements:
    if os.path.isfile(os.path.join(path, el)):  
        allFiles.append(el)

print("Directories", allDirs)
print("Files", allFiles)
print("All directories, files", allElements)