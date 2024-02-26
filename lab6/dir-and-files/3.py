#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def analys(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")
    else:
        print(f"The path '{path}' does not exist.")

path = r"C:\Users\User\Documents\uni\pp2\lab6\builtin_functions"
analys(path)