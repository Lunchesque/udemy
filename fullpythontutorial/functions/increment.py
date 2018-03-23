# total = 0
# def increment():
#     total += 1
#     return total
#
# increment() # error


total = 0
def increment():
    global total
    total += 1
    return total

print(increment())
