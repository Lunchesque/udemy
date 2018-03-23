def sum_odd_number(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_number([1, 2, 3, 4, 5, 6, 7]))
