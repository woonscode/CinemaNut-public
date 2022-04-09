# Code Snippets

import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "8c3ee30dfcmsh1b2042bd6f9f5e1p1fcd92jsn6ffac72ad451"
    }

conn.request("GET", "/title/details?netflix_id=70143836", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Results

{
  "title": "Breaking Bad",
  "maturity_label": "Suitable for mature audiences only",
  "maturity_level": "110",
  "synopsis": "A terminally ill chemistry teacher teams with a former student to manufacture crystal meth to secure his family&#39;s future.",
  "title_type": "series",
  "default_image": "https://occ-0-2851-38.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABcRDr6fbQ5zoGWrY4qVN7P3paEOOf_sVG1WbrTYzL2KmfWZdAFfReDl_r7y2-PC17h6nUA6PP9D9yIEBRwS5OTI4pQ.jpg?r=a1e",
  "large_image": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABW8ZgA4rIVS2cOVVFOHnJFAEtN_FesWd0xCSVaoejuTyrKxk5IzGZF-3lGkiS7E0sU05luFuv3yzsMqnk2zzWV8yVept.jpg?r=a1e",
  "netflix_id": "70143836",
  "start_date": "2015-04-14",
  "latest_date": "2022-03-15",
  "year": "2008",
  "poster": "",
  "runtime": "",
  "awards": "",
  "origin_country": "",
  "rating": "",
  "alt_id": "tt0903747",
  "alt_plot": "",
  "alt_metascore": "",
  "alt_votes": "1391850",
  "alt_runtime": "0",
  "alt_image": ""
}