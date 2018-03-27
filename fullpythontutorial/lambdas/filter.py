# list1 = [1,2,3,4,5,6]
# evens = list(filter(lambda x: x % 2 == 0, list1))
# print(evens)

# names = ["austin", "penny", "anthony", "angel", "billy"]
# a_names = filter(lambda n: n[0] == "a", names)
# print(list(a_names))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# inactive_users = list(filter(lambda u: not u["tweets"], users))
# print(inactive_users)

inactive_users2 = [user["username"].upper() for user in users if not user["tweets"]]
# print(inactive_users2)

# usernames = list(map(lambda user: user["username"].upper(),
#     filter(lambda u: not u["tweets"], users)))
# print(usernames)

def remove_negatives(nums):
    return list(filter(lambda num: num >= 0, nums))
print(remove_negatives([1,2,-3, 0, -100, -3,213]))
