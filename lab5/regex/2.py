#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def ab23(text):
    pattern = "ab{2,3}"
    if re.fullmatch(pattern, text):
        return "Match found"
    else:
        return "No match"
    
print(ab23(data))