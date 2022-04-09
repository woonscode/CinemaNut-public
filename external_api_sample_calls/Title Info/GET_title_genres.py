# Code Snippets

import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "8c3ee30dfcmsh1b2042bd6f9f5e1p1fcd92jsn6ffac72ad451"
    }

conn.request("GET", "/title/genres?netflix_id=70143836", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Results

{
    "Object": {
        "total": 5,
        "limit": 100,
        "offset": 0
    },
    "results": [
        {
            "genre_id": 72404,
            "genre": "US TV Programmes"
        },
        {
            "genre_id": 11714,
            "genre": "TV Dramas"
        },
        {
            "genre_id": 83,
            "genre": "TV Programmes"
        },
        {
            "genre_id": 26009,
            "genre": "Crime TV Dramas"
        },
        {
            "genre_id": 89811,
            "genre": "TV Thrillers"
        }
    ]
}