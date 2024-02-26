#Write a Python program to copy the contents of a file to another file
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            contents = source.read()
            destination.write(contents)
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file_path = r"C:\Users\User\Documents\uni\pp2\A.txt"
destination_file_path = r"C:\Users\User\Documents\uni\pp2\B.txt"

copy_file(source_file_path, destination_file_path)