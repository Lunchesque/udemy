# def devide(num1, num2):
#     return num1/num2
#
# print(devide(100, 5))
# print(devide(5, 3))


def yell(string1):
    """YELLING

    >>> yell("hello")
    'HELLO!'

    >>> yell(111)
    Traceback (most recent call last):
        ...
    AttributeError: 'int' object has no attribute 'upper'
    """
    return string1.upper() + "!"

print(yell("go away"))
