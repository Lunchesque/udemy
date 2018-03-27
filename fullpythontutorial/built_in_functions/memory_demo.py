import sys
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do same thing, it takes...")
print("List comprehension: {} bytes".format(list_comp))
print("Generator expression: {} bytes".format(gen_exp))
