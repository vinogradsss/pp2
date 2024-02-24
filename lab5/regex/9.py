#Write a Python program to insert spaces between words starting with capital letters.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def insert(str):
    result = re.sub(r"([A-Z][a-z]+)", r" \1", str) #space and \1 - found match of pattern
    return result

print(insert(data))