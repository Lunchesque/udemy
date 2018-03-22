"""
SYNTAX:
[first_variable for variable in second_variable]
"""
# nums = [1, 2, 3]
# print([x*2 for x in nums])

# names = ["Elie", "Tim", "Matt"]
# answer = [name[0] for name in names]
# print(answer)
#
# numbers = [1, 2, 3, 4, 5, 6]
# answer2 = [num for num in numbers if num % 2 == 0]
# print(answer2)

# one = [1, 2, 3, 4]
# two = [3, 4, 5, 6]
# answer = [num for num in one if num in two]
# print(answer)
# words = ["Elie", "Tim", "Matt"]
# answer2 = [word[::-1].lower() for word in words]
# print(answer2)

# numbers = range(1, 101)
# answer = [num for num in numbers if num % 12 == 0]
# print(answer)

answer = [char for char in "amazing" if char not in "aeiou"]
print(answer)
