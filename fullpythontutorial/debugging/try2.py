# try:
#     num = int(input("Please inter a number: "))
# except:
#     print("This is not a number")
# else:
#     print("Im the else")
# finally:
#     print("im running no matter what happened")

while True:
    try:
        num = int(input("Please inter a number: "))
    except ValueError:
        print("This is not a number")
    else:
        print("good, its a number")
        break
    finally:
        print("im running no matter what happened")
print("rest of game logic")
