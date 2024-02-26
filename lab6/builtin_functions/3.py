#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(str):
    str = str.lower()
    inverse = str[::-1]
    return str == inverse

example = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(example):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")