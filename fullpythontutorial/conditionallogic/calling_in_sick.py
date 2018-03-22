from random import choice, randint

actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)

print("actually_sick = " + str(actually_sick))
print("kinda_sick = " + str(kinda_sick))
print("hate_your_job = " + str(hate_your_job))
print("sick_days = " + str(sick_days))
print("###############")

calling_in_sick = None

if actually_sick and sick_days > 0:
    calling_in_sick = True
    print(calling_in_sick)
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
    print(calling_in_sick)
else:
    calling_in_sick = False
    print(calling_in_sick)
