#Write a Python program to count the number of lines in a text file.
def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Number of lines in the file: {num_lines}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IsADirectoryError:
        print(f"'{file_path}' is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred: {e}")

path = r"C:\Users\User\Documents\uni\mpge\Example.docx"

count_lines(path)