def multiply_even_numbers(list1):
    result = 1
    for i in list1:
        if i % 2 == 0:
            result *= i
    return result


print(multiply_even_numbers([1, 2, 3, 4, 5]))
