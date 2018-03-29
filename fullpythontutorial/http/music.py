import requests
"""
https://music.mts.by/handlers/search.jsx
"""

url = "https://music.mts.by/handlers/search.jsx"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"text": "bon jovi - it's my life"}
    ).json()
songs = response["tracks"]["items"]
for song in songs:
    print(song["title"])
