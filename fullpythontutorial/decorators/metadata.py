from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """its the wrapper function"""
        print("You are about to call {}".format(fn.__name__))
        print("Here is the doumentation: {}".format(fn.__doc__))
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
    """adds two numbers together"""
    return x + y

# print(add(10, 20))
print(add.__name__)
print(add.__doc__)
help(add)
