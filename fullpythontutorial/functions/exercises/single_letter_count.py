def single_letter_count(str1, str2):
    times = 0
    for char in str1:
        if str2.lower() == char.lower():
            times += 1
    return times

print(single_letter_count("abra kadabra", "z"))
