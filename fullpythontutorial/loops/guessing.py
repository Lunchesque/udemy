import random
random_number = random.randint(1, 10)
guess = ""
while guess != random_number:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess < random_number:
        print("your choise is lower")
    elif guess > random_number:
        print("your coise is higher")
print("you got it")
