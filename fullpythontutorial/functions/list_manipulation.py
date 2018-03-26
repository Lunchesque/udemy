def list_manipulation(list1, command, location, value=None):
    if command == "remove" and location == "end":
        return list1.pop()
    elif command == "remove" and location == "beginning":
        return list1.pop(0)
    elif command == "add" and location == "beginning":
        list1.insert(0, value)
        return list1
    elif command == "add" and location == "end":
        list1.insert(len(list1), value)
        return list1

print(list_manipulation([1,2,3], "add", "end", 30))
