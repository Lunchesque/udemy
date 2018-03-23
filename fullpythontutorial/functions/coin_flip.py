from random import random

# def flip_coin():
#     # generate a random number from 0-1
#     r = random()
#     if r >= 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# def flip_coin():
#     if random() >= 0.5:
#         return "HEADS"
#     else:
#         return "TAILS"
#
# print(flip_coin())

def generate_evens():
    return [i for i in range(1, 50) if i % 2 == 0]
print(generate_evens())
