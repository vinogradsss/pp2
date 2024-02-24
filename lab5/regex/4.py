#Write a Python program to find the sequences of one upper case letter followed by lower case letters.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def find_seq(text):
    pattern = r"[A-Z][a-z]+"
    match = re.findall(pattern, text)   
    return match

print(find_seq(data))