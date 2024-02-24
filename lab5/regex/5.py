#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def match_str(text):
    pattern = r"a.*b$"
    if re.search(pattern, text):
        return "Match found"
    else:
        return "Match not found"

print(match_str(data))