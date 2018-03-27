def max_magnitude(nums):
    return max(abs(num) for num in nums)
print(max_magnitude([200, 23, -400, 300]))

def sum_even_values(*values):
    return sum(val for val in values if val % 2 == 0)
print(sum_even_values(1,3,4,6,7))

def sum_floats(*floats):
    return sum(arg for arg in floats if type(arg) == float)
print(sum_floats(1,2,3,4,6))
print(sum_floats(1, "asfa", 4.32, 32, True, 1.01))
