# while True:
#     command = input("Type 'exit' to exit: ")
#     if command == "exit":
#         break

# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break
#
# i = 0
# while i <= 5:
#   i =+ 1
#   print(i)

from random import randint

number = 0
i = 0

while number != 5:
    number = randint(1, 10)
    i += 1
print(i)
