# def ensure_correct_info(*args):
#     if "Colt" in args and "Steele" in args:
#         return("Welcome back Colt")
#     return "Not sure who you are"
#
# print(ensure_correct_info("HELLO", 34, True))
# print(ensure_correct_info(1, False, "Steele", "Colt"))

def contains_purple(*args):
    if "purple" in args:
        return True
    return False

print(contains_purple(1, "dalfkjds", 1.42, "kdfkd"))
print(contains_purple(1, "dalfkjds", 1.42, "purple"))
