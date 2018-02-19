

def exeptions():
    try:
        car = {"make" : "audi", "model" : "A8", "year" : 2018}
        print(car["color"])
    except:
        print("None colored car")
    finally:
        print("'finaly' executes always")

exeptions()