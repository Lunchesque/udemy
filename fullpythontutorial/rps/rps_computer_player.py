import random
print("Rock...\nPaper...\nScissors...")

player = input("Enter your choice: ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print("Computer choice is: " + computer)

if player == computer:
    print("Draw")
elif player == "rock" and computer == "paper":
    print("Computer wins")
elif player == "rock" and computer == "scissors":
    print("Player wins")
elif player == "paper" and computer == "scissors":
    print("Computer wins")
elif player == "paper" and computer == "rock":
    print("Player wins")
elif player == "scissors" and computer == "rock":
    print("Computer wins")
elif player == "scissors" and computer == "paper":
    print("Player wins")
else:
    print("something went wrong")
