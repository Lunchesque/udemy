from time import time
from functools import wraps

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print("Executing {}".format(fn.__name__))
        print("Time Elapsed: {}".format(end_time - start_time))
        return result
    return wrapper

@speed_test
def sum_nums_generator():
    return sum(x for x in range(300000000))
print(sum_nums_generator())

@speed_test
def sum_nums_list_comprehencion():
    return sum([x for x in range(300000000)])
print(sum_nums_list_comprehencion())
