def compact(list1):
    """ Printing only True values of the list

    >>> compact(["", 1, False, True, "js"])
    [1, True, 'js']

    >>> compact([False, '', 0])
    []
    """
    return [val for val in list1 if val]

print(compact(["", 1, False, True, "js"]))
print(compact([False, '', 0]))
