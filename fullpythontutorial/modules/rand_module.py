# from random import choice, randint
#
# print(choice(["apple", "banana", "cherry", "durian"]))
# print(randint(1, 100))
# random.shuffle(["apple", "banana", "cherry", "durian"])
# import math
# answer = math.sqrt(15129)
# print(answer)

import keyword
def contains_keyword(*strs):
    for s in strs:
        if keyword.iskeyword(s):
            return True
    return False

print(contains_keyword("orca", "shark", "return"))
print(contains_keyword("def", "askdjkas", "bye", "word", "2345"))
