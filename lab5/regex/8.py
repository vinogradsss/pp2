#Write a Python program to split a string at uppercase letters.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def split(str):
    splitted = re.findall(r"[A-Z][^A-Z]*", str)
    return splitted

print(split(data))