# Get all filenames in a folder

import os

files = []
folder = os.listdir("HHB/multiple_files")

for file in folder:
    if file.endswith(".csv"):
        files.append(file)

print(files)