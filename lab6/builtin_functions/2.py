#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count(str):
    up = 0
    low = 0
    
    for char in str:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
    
    return up, low

example = input("Enter the string: ")

upper, lower = count(example)

print("Number of upper case characters : ", upper)
print("Number of lower case characters : ", lower)