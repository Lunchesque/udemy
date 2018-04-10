# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive"
#     return x + y
#
# print(add_positive_numbers(1, 2))
# print(add_positive_numbers(1, -1))

def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
        ], +"food must be a junk food"

    return "num num num, nice {}".format(food)

food = input("Enter a food: ")
print(eat_junk(food))
