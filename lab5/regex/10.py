#Write a Python program to convert a given camel case string to snake case.
import re
with open(r"C:\Users\User\Documents\уник\pp2\lab5\regex\row.txt", 'r', encoding='UTF-8') as file:
        data = file.read()

def c_to_s(camel):
    snake = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", camel)# \1 - lower case or digits and \2 - upper case and _ between them
    snake = snake.lower()
    return snake

print(c_to_s(data))