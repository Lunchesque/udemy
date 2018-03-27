# nums = [4,5,6,2,3,43,8]
# print(sorted(nums))
# print(sorted(nums, reverse=True))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# print(sorted(users, key=lambda user: user["username"]))
print(sorted(users, key=lambda user: len(user["tweets"])))
