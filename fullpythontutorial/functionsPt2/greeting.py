# def special_greeting(**kwargs):
#     if "David" in kwargs and kwargs["David"] == "special":
#         return "You get a special greeting David"
#     elif "David" in kwargs:
#         return "{} David!".format(kwargs["David"])
#
#     return "Not sure who is this..."
#
# print(special_greeting(David="hello"))
# print(special_greeting(David="Hello"))
# print(special_greeting(David="special"))

def combine_words(word, **kwargs):
    if "prefix" in kwargs.keys():
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word

print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("child"))
