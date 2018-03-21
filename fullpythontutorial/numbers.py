# for x in range(1, 21):
#     if x % 2 == 1:
#         if x == 13:
#             print("{}: UNLUCKY!".format(x))
#         print("{}: is odd".format(x))
#     elif x % 2 == 0:
#         if x == 4:
#             print("{}: UNLUCKY!".format(x))
#         print("{}: is even".format(x))


for x in range(1, 21):
    if x == 4 or x == 13:
        state = "UNLUCKY!"
    elif x % 2 == 1:
        state = "odd"
    else:
        state = "even"
    print("{}: is {}".format(x, state))
