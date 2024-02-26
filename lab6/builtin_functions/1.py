#Write a Python program with builtin function to multiply all the numbers in a list
def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

example = [1, 2, 3, 4, 5]
result = multiply_numbers(example)
print("Result is:", result)