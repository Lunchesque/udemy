import random
random_number = random.randint(1, 10)
guess = None
while True:
    guess = int(input("Pick a number from 1 to 10: "))
    if guess < random_number:
        print("your choise is lower")
    elif guess > random_number:
        print("your coise is higher")
    else:
        print("you got it")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            random_number = random.randint(1, 10)
            guess = None
        else:
            print("thanks for playing")
            break
