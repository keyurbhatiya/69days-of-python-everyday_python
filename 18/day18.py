################################## Day 18: 69 Days of Python #####################################

# Automating folders using os module

import os
import shutil


# Get current working directory
print("Current Directory:", os.getcwd())


print("---------------------------------------------------")


# Create a new folder
folder_name = "demo_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Folder created:", folder_name)
else:
    print("Folder already exists")


print("---------------------------------------------------")


# Create multiple folders
folders = ["Images", "Documents", "Videos"]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Created:", folder)


print("---------------------------------------------------")


# List all files and folders
items = os.listdir()
print("Files & Folders:")
for item in items:
    print(item)


print("---------------------------------------------------")


# Rename a folder
if os.path.exists("demo_folder"):
    os.rename("demo_folder", "renamed_folder")
    print("Folder renamed successfully")


print("---------------------------------------------------")


# Move a file (example)
# Make sure example.txt exists before running this
if os.path.exists("example.txt"):
    shutil.move("example.txt", "Documents/example.txt")
    print("File moved successfully")


print("---------------------------------------------------")


# Remove an empty folder
if os.path.exists("renamed_folder"):
    os.rmdir("renamed_folder")
    print("Folder removed")


print("--------------------------------------------------- End of Day 18 ---------------------------------------------------")
