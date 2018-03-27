class SpecialList:
    def __init__(self, data):
        self.__data = data

    def __len__(self):
        return 50

l1 = SpecialList([1, 40, 30, 100])
print(len(l1))
