def isEven(num):
    return num % 2 == 0

def partition(list1, isEven):
    truthy_list = []
    falsy_list = []
    for num in list1:
        if isEven(num):
            truthy_list.append(num)
        else:
            falsy_list.append(num)
    return [truthy_list, falsy_list]

print(partition([1,2,3,4], isEven))
