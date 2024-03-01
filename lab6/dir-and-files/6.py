#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        with open(file_name, "w") as file:
            file.write(f"This is the content of {file_name}")

generate_text_files()