"""
SYNTAX
{____:____ for___in____}
"""

# numbers = dict(first=1, socond=2, third=3)
# print(numbers)
# squared_numbers = {key:value ** 2 for key,value in numbers.items()}
# print(squared_numbers)

# dict_one = {num: num ** 2 for num in [1, 2, 3, 4, 5]}
# print(dict_one)

# str1 = "ABC"
# str2 = "123"
# combo = {str1[i]: str2[i] for i in range(0, len(str1))}
# print(combo)

num_list = [1, 2, 3, 4]
num_dict = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(num_dict)
