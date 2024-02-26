#Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            print(f"Path '{file_path}' exists.")

            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File '{file_path}' deleted successfully.")
            else:
                print(f"No write access to file '{file_path}'.")
        else:
            print(f"Path '{file_path}' does not exist.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred: {e}")

file = r"C:\Users\User\Documents\uni\pp2\C.txt"
delete_file(file)