def  fav_colors(**kwargs):
    for person, color in kwargs.items():
        print("{} fav color is {}".format(person, color))

fav_colors(colt="purple", ruby="red", ethel="teal")
