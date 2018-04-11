import os

# f = open("story.txt")
# print(f.read())
# print(f.closed)
# f.close()
# print(f.closed)

with open("story.txt") as file:
    print(file.read())

print(file.closed)
