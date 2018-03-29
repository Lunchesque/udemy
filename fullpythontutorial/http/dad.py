import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

print(colored(figlet_format("Jokes art"), color="yellow"))

def print_joke():
    about = input("Let me tell a joke! Give me a topic: ")
    _num_of_jokes = len(get_jokes(about))
    if _num_of_jokes > 1:
        return "I have a cuple of joke on this theme, here is one of them:\n{}".format(choice(get_jokes(about)))
    elif _num_of_jokes == 0:
        return("I have no jokes about for this theme")
    return "Here is the joke:\n{}".format(choice(get_jokes(about)))

def get_jokes(about):
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(
        url,
        headers={"Accept": "application/json"},
        params={"term": about}
        )
    data = response.json()
    return [joke["joke"] for joke in data["results"]]

print(print_joke())
