# numbers = [3, 3, 3, 4, 6, 6, 1, 1, 1, 90, 34]
# print(numbers)
"""
index
"""
# print(numbers.index(3))
# print(numbers.index(90))
# print(numbers.index(3, 1))
# print(numbers.index(1, 7, 10))
"""
count
"""
# print(numbers.count(3))
# print(numbers.count(6))
# print(numbers.count(21))
"""
reverse
"""
# numbers.reverse()
# print(numbers)
"""
sort
"""
# numbers.sort()
# print(numbers)
"""
join
"""
# words = ["coding", "is", "fun!"]
# print(' '.join(words))


# Create a list called instructors
instructors = []
# Add the following strings to the instructors list
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt", "Blue", "Lisa"])
# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0, "Done")
print(instructors)
