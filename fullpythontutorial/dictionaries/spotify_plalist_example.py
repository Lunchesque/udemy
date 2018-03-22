playlist = {"title": "patagonia bus",
            "author" : "colt steele",
            "songs": [
                {"title": "song1", "artist": ["artist1"], "duration": 2.5},
                {"title": "song2", "artist": ["artist2", "dj cat"], "duration": 5.25},
                {"title": "nice song", "artist": ["various artist"], "duration": 3.1}
            ]
}

total_length = 0
for song in playlist["songs"]:
    total_length += song["duration"]
print(total_length)
