def is_palindrome(value):
    list1 = [char.lower() for char in value if char != " "]
    return list1 == list1[::-1]
print(is_palindrome("man a plan a canal Panama"))
