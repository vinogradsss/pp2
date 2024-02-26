#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def list_dir_and_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

example_path = r"C:\Users\User\Documents\uni\mpge"

directory_path = os.path.dirname(example_path)

print("List of directories and files in the specified directory:")
list_dir_and_files(directory_path)