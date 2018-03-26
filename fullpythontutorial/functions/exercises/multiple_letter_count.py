def multiple_letter_count(str1):
    return {value: str1.count(value) for value in str1}

print(multiple_letter_count("ololo"))
