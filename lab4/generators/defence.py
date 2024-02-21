def even_num(b):
    for i in range(1, b + 1):
        if i % 2 == 0:
            yield i
        
x = int(input("Enter the number: "))
for n in even_num(x):
    print(n)