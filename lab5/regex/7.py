#Write a python program to convert snake case string to camel case string.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def s_to_c(snake):
    camel = re.sub(r"(?:^|_)([a-z])", lambda match: match.group(1).upper(), snake)
    return camel

print(s_to_c(data))