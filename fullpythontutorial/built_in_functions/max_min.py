# names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
# print(min(names))

# print(min(len(name) for name in names))

# print(max(names, key=lambda n: len(n)))
# print(min(names, key=lambda n: len(n)))
"""
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda s: s["playcount"]))
print(max(songs, key=lambda s: s["playcount"])["title"])
"""

def extremes(values):
    return (min(values), max(values))
print(extremes([1,2,3,4,67,8]))
