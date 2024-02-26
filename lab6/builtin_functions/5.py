#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def check(t):
    return all(t)

t1 = (True, True, True)
t2 = (True, False)
t3 = () 

print(f"All elements in {t1} are true: {check(t1)}")
print(f"All elements in {t2} are true: {check(t2)}")
print(f"All elements in {t3} are true: {check(t3)}")