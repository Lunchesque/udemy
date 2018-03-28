import pdb

# first = "Fisrst"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

# def add_numbers(a,b,c,d):
#     import pdb; pdb.set_trace()
#
#     return a+b+c+d
# add_numbers(1,2,3,4)

def devide(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        print("Please provide two integers or floats")
    except ZeroDivisionError:
        print("Please do not divide by zero")
print(devide(1,2))
print(devide([], "1"))
print(devide(1,0))
