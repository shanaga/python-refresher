def prod(a, b):
    return a * b


def factorial_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        i = i + 1
        n = output

#Test Block
my_gen = factorial_gen()
num = 6
for i in range(num):
    print(next(my_gen))

