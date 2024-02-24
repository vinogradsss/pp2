#Write a Python program to find sequences of lowercase letters joined with a underscore.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def check(text):
    return re.findall(r"\b[a-z]+_[a-z]+\b", text)

print(check(data))