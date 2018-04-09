from functools import wraps

def ensure_na_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed")
        return fn(*args, **kwargs)
    return wrapper

@ensure_na_kwargs
def greet(name):
    print("Hello {}".format(name))

greet(name="Tom")
