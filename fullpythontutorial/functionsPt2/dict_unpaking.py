def display_names(first, second):
    print("{} say hello to {}".format(first, second))

names = {"first": "Colt", "second": "Rusty"}

display_names(**names)
