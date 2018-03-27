# midterms = [80, 91, 78]
# finals = [98, 89, 53]
# students = ["dan", "ang", "kate"]

# final_grades = [max(pair) for pair in zip(midterms, finals)]

# final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}

# grades = zip(
#     students,
#     map(
#         lambda pair: max(pair),
#         zip(midterms, finals)
#     )
# )
# print(dict(grades))

# def interleave(str1, str2):
#     r = []
#     for val in list(zip(str1, str2)):
#         r.append("".join(v for v in val))
#     for val in r:
#         return "".join(v for v in r)

# def interleave(str1,str2):
#     return ''.join(''.join(x) for x in (zip(str1,str2)))
# print(interleave("hi", "no"))
# print(interleave("aaa", "zzz"))

# def triple_and_filter(nums):
#     return [num*3 for num in nums if num % 4 == 0]
# print(triple_and_filter([1,2,3,4,5,6,7,8]))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']
