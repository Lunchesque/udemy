def sum(n, func):
    total = 0
    for i in range(1, n+1):
        total += func(i)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print(sum(3, cube))
print(sum(3, square))
