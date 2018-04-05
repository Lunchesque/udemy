def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)

def square(x):
    print(x*x)

# my_for("lol", print)
my_for([1,2,3,4], square)
