days = {1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
        }

def return_day(key):
    if key in days.keys():
        return days[key]
    return None

print(return_day(45))
