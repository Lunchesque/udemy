# def devide(a,b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("You cant devide by ZERO")
#     except TypeError as err:
#         print("a and b must ints or floats")
#         print(err)
#     else:
#         print("{} devided by {} is: {}".format(a,b,result))

def devide(a,b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError) as err:
        print("Something went wrong!")
        print(err)
    else:
        print("{} devided by {} is: {}".format(a,b,result))

print(devide(1, 2))
print(devide(1, 0))
print(devide(1, "d"))
