import os
from pathlib import Path

"""
goal of this code is, to remove duplicate files in all folders and subfolders
First all files will be listed or written into a txt file
then a txt file will be generated to list all duplicate files
then the duplicates can be removed.

to identify a duplicate file, i need to check for file name and also for meta data for the creation date.
1: get file name and creation date
2: list all filenames with theire creation date and write into a txt file
3: write all duplicate files into a txt file
4: remove the duplicate files
"""

location = "C:/Users/LoCaMi/OneDrive/Programmieren/Projects/File Manager/files"
cwd = os.getcwd() # get the current working directory

files_before = os.listdir(location)

print(files_before)

file = "test1.txt"
path = os.path.join(location, file) 

# os.remove(path)

# files_after = os.listdir(location)
# print(files_after)


"""
Check if path is file, else recursive call delete duplicate
compare not the file name and creation date, instead compare the file hashes.
"""

# getting only files 
for file in os.listdir(location):   # looping over the file list

    file_name = Path(os.path.join(location, file))  # make a absolute file name using os.path.join function
    if file_name.is_file():  # checking the the the item is file or not
        print(file)
    else:
        print(f"Folder: {file}")