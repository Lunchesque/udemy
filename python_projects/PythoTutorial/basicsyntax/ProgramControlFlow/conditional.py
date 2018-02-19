"""
Conditional Logic
"""

if 100 > 10:
    print("Hundred is greater than 10")

value = input("Input value (options: red/green/yellow):\n")

if value == 'green':
    print("Go")
elif value == 'yellow':
    print("Prepare to stop")
elif value == "red":
    print("Stop")
else:
    print("We have no value like this")

print("It will always print")
