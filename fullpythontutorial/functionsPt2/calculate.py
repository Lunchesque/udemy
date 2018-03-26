def calculate(make_float, operation , first, second, message="The result is"):
    if operation == "add":
        if make_float == False:
            return "{} {}".format(message, int(first + second))
        return "{} {}".format(message, float(first + second))
    elif operation == "subtract":
        if make_float == False:
            return "{} {}".format(message, int(first + second))
        return "{} {}".format(message, float(first - second))
    elif operation == "multiply":
        if make_float == False:
            return "{} {}".format(message, int(first + second))
        return "{} {}".format(message, float(first * second))
    elif operation == "divide":
        if make_float == False:
            return "{} {}".format(message, int(first + second))
        return "{} {}".format(message, float(first / second))

print(calculate(make_float=True, operation='divide', first=3.5, second=5))
print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
