def capitalize(string1):
    """ Capitalize first letter

    >>> capitalize('sergey')
    'Sergey'

    >>> capitalize(1)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not subscriptable
    """
    return string1[0].upper() + string1[1::1]

print(capitalize("sergey"))
# print(capitalize(1))
