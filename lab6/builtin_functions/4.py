#Write a Python program that invoke square root function after specific milliseconds
import time
import math

def delayed_root(n, delay):
    delay_seconds = delay / 1000.0
    time.sleep(delay_seconds)
    
    result = math.sqrt(n)
    print(f"The square root of {n} after {delay} miliseconds is {result}.")

example = int(input("Enter the number: "))
delay = int(input("Enter the time for delay: "))
delayed_root(example, delay)