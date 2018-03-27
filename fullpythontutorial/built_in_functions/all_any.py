# people = ["Charlie", "Casey", "Cody", "Carly", "Cristina"]
# l = [name[0] == "C" for name in people]
# print(l)
# print(all(l))

# nums = [2,60,26,18,21]
# print(any([num % 2 == 1 for num in nums]))
# print(any([num % 2 == 0 for num in nums]))

def is_all_strings(list1):
    return all(type(val) == str for val in list1)

print(is_all_strings(["a", "s", "s", "t"]))
print(is_all_strings([2, "das", "fa", "as"]))
print(is_all_strings(("asdfa", "dasfas")))
