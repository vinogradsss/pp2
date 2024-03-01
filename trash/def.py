#файл тtxt и регекс чтобы в строке была олна заглавная буква, хотя бы одно число и все остльное лоуер
import re    
file = open(r"C:\Users\User\Documents\uni\pp2\trash\defence.txt", "r")
data = file.read()

pattern = "[A-Z]{1}[a-z]+[0-9]"

example = re.findall(pattern, data)
print(example)