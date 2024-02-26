#Write a Python program to write a list to a file.
def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("List successfully written to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

path = r"C:\Users\User\Documents\uni\mpge\Example.docx"

listik = ["apple", "banana", "orange", "grape"]

write_list_to_file(path, listik)