class GrumpyDict(dict):
    def __repr__(self):
        print("none of your business")
        return super().__repr__()

    def __missing__(self, key):
        print("you want {}? its not here".format(key))

    def __setitem__(self, key, value):
        print("change dict")
        super().__setitem__(key, value)

data = GrumpyDict({"name": "jack", "city": "M"})
print(data)
data["asdf"] = "asdf"
print(data)
