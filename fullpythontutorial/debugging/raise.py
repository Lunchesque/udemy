# raise ValueError("Invalid value")
def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(color) is not str:
        raise TypeError("color must be a string")
    if type(text) is not str:
        raise TypeError("text must be a string")
    if color not in colors:
        raise ValueError("color is Invalid")
    print("Printed {} in {}".format(text,color))

colorize([], "cyan")
# colorize(444, "red")
