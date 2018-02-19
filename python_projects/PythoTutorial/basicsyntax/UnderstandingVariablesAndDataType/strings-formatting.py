"""
Examples to show how string formatting works in python
"""

city = "nyc"
event = "show"

print("Welcome to " + city + " and enjoy the " + event)
print("Welcome to %s" % city)
print("Enjoy the %s" % event)
print("Welcome to %s and enjoy the %s" % (city, event))
print("Welcome to {} and enjoy the {}".format(city, event))
print("Welcome to {0} and enjoy the {1}".format(city, event))