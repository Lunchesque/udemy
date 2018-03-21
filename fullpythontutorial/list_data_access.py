# colors = ["purple", "yellow", "red"]
# print(len(colors))

# print(colors[0])
# print(colors[1])
# print(colors[2])
#
# print(colors[-1])
# print(colors[-2])
# print(colors[-3])
#
# print("red" in colors)
# print("dsfkjdskl" in colors)
# print("yellow" in colors)
#
# people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# people[0] = "Hannah"
# people[-2] = "Jeffrey"
# people[-1] = "Aparna"
# print(people)
#
# numbers = [1, 2, 3, 4]
# for num in numbers:
#     print(num)
#
numbers = [4, 6, 2, 9, 7, 10]
# for num in numbers:
#     print(num * num)
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for i in sounds:
    result += i.upper()
print(result)
