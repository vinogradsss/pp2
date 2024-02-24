#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

pattern = r"/w*ab*/w*"

example = re.findall(pattern, data)
print(example)