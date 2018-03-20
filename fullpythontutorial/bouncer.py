# ask for age
age = input("How old are you?\n")
if age:
    age = int(age)
    if age >= 21:
        print("you good to go and drink!")
    elif age >=18:
        print("go in, but get wristband")
    else:
        print("you are too young")
else:
    print("enter age")
