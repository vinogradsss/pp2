#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def replace(text):
    pattern = r"[ ,.]"
    replaced = re.sub(pattern, ":", text)
    return replaced

print(replace(data))