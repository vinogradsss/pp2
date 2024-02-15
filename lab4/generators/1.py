#Create a generator that generates the squares of numbers up to some number N.
def square_gen(N):
    for i in range(1, N + 1):
        yield i ** 2

n = int(input("Enter the number: "))
for k in square_gen(n):
    print(k)