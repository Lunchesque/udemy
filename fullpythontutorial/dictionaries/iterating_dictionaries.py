instructor = {
    "name": "Colt",
    "owns_dog": False,
    "num_courses": 4,
    "fav_language": "Python",
    "is_hilarious": True,
    "fav_num": 17
}
# Iterating through values
# for value in instructor.values():
#     print(value)

# Iterating through keys
# for key in instructor.keys():
#     print(key)

# Iterating through both values and keys
# for item in instructor.items():
#     print(item)

# for key, value in instructor.items():
#     print("{}: {}".format(key, value))


donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
print(sum(donations.values()))
