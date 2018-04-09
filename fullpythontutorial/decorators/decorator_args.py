# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return "Hi i'm {}".format(name)

@shout
def order(main, side):
    return "i want {}, with a side of {} pls".format(main, side)

@shout
def lol():
    return "lol"

print(greet("matt"))
print(order("burger", "fries"))
print(lol())
