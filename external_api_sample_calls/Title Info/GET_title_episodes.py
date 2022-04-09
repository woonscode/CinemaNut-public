# Code Snippets

import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "8c3ee30dfcmsh1b2042bd6f9f5e1p1fcd92jsn6ffac72ad451"
    }

conn.request("GET", "/title/episodes?netflix_id=70143836&season_id=70105286", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Results

{
    "Object": {
        "total": 7,
        "limit": 100,
        "offset": 0
    },
    "results": [
        {
            "netflix_id": 0,
            "episode_id": 70196252,
            "season_id": 70105286,
            "episode_number": "1",
            "season_number": "1",
            "synopsis": "Diagnosed with terminal lung cancer, a high school chemistry teacher resorts to cooking and selling methamphetamine to provide for his family.",
            "title": "Pilot",
            "image": "https:# occ-0-2219-2218.1.nflxso.net/art/cdb03/cc2ba1e3d0b88b12101cb7842b059800c6ccdb03.jpg"
        },
        {
            "netflix_id": 0,
            "episode_id": 70196253,
            "season_id": 70105286,
            "episode_number": "2",
            "season_number": "1",
            "synopsis": "Their first aborted drug deal forces Walt and Jesse to dispose of a pair of corpses. Meanwhile, Skyler suspects that her husband is up to no good.",
            "title": "The Cat&#39;s in the Bag",
            "image": "https://occ-0-2219-2218.1.nflxso.net/art/0d33f/ec5861106f3c6d8b891d3b7dbe3dc1f64790d33f.jpg"
        },
        {
            "netflix_id": 0,
            "episode_id": 70196254,
            "season_id": 70105286,
            "episode_number": "3",
            "season_number": "1",
            "synopsis": "As Walt cleans up the mess that was left after his first drug deal, Skyler gets too close to the truth about his double life.",
            "title": "And the Bag&#39;s in the River",
            "image": "https://occ-0-2219-2218.1.nflxso.net/art/9560e/2dd77d0584f88d521164377bd292add8be69560e.jpg"
        },
        {
            "netflix_id": 0,
            "episode_id": 70196255,
            "season_id": 70105286,
            "episode_number": "4",
            "season_number": "1",
            "synopsis": "Being forced to reveal the truth about his illness leaves Walt facing the dilemma of how to pay for an expensive series of cancer treatments.",
            "title": "Cancer Man",
            "image": "https://occ-0-2219-2218.1.nflxso.net/art/09fcf/b8e0ba2b67ce478d9036da80ec60b19b74909fcf.jpg"
        },
        {
            "netflix_id": 0,
            "episode_id": 70196256,
            "season_id": 70105286,
            "episode_number": "5",
            "season_number": "1",
            "synopsis": "Skyler organizes an intervention to persuade Walt to accept his former research partner&#39;s generous offer to pay for the cancer treatments.",
            "title": "Gray Matter",
            "image": "https://occ-0-2219-2218.1.nflxso.net/art/4864c/ad91f14f390368b40dd6a2b123f5ead4f634864c.jpg"
        },
        {
            "netflix_id": 0,
            "episode_id": 70196257,
            "season_id": 70105286,
            "episode_number": "6",
            "season_number": "1",
            "synopsis": "With the side effects and cost of his treatment mounting, Walt demands that Jesse find a wholesaler to buy their drugs -- which lands him in trouble.",
            "title": "Crazy Handful of Nothin&#39;",
            "image": "https://occ-0-2219-2218.1.nflxso.net/art/ec4b6/b9ee5c1de53b924b9d660607855ac7390ddec4b6.jpg"
        },
        {
            "netflix_id": 0,
            "episode_id": 70196258,
            "season_id": 70105286,
            "episode_number": "7",
            "season_number": "1",
            "synopsis": "After Jesse&#39;s brush with death, Walt agrees to produce even more drugs for the ruthless Tuco. Meanwhile, Skyler suspects her sister of shoplifting.",
            "title": "A No-Rough-Stuff-Type Deal",
            "image": "https://occ-0-2219-2218.1.nflxso.net/art/f4fdc/5cc8278b5978a428c0114e1c1b4895198c1f4fdc.jpg"
        }
    ]
}