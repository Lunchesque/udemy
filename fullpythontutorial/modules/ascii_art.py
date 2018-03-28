from pyfiglet import figlet_format
from termcolor import colored
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
msg = input("What you need to print? ")
color = input("What color? ")


def formated_text(text, color):
    while color not in valid_colors:
        color = input(
            "valid colors are{}\nEnter a valid color: ".format(valid_colors))
    ascii_art = figlet_format(msg)
    return colored(ascii_art, color=color)


print(formated_text(msg, color))
