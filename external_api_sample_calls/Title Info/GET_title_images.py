# Code Snippets

import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "8c3ee30dfcmsh1b2042bd6f9f5e1p1fcd92jsn6ffac72ad451"
    }

conn.request("GET", "/title/images?netflix_id=70143836", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Results

{
    "Object": {
        "total": 41,
        "limit": 100,
        "offset": 0
    },
    "results": [
        {
            "url": "http://art-2.nflximg.net/45884/aa20cb9912c9320cb00b1c392d826f94f4445884.jpg",
            "image_type": "boxart"
        },
        {
            "url": "http://art-2.nflximg.net/8bb20/a78fc7390503fd37a6629e365fed555c9068bb20.jpg",
            "image_type": "boxart"
        },
        {
            "url": "http://art-2.nflximg.net/c12d1/2fc5897a715bac6b6caa99ad84ea53c5638c12d1.jpg",
            "image_type": "boxart"
        },
        {
            "url": "http://art-2.nflximg.net/d7bc4/dc51e2cf64ca79cf0b94c7f995927ddd76dd7bc4.jpg",
            "image_type": "boxart"
        },
        {
            "url": "http://art-2.nflximg.net/eb333/a2996f4b8c793b18d80213475e09fc5762beb333.jpg",
            "image_type": "boxart"
        },
        {
            "url": "http://occ-2-768-769.1.nflxso.net/art/10825/d2c17a657ef26af04d19cf46a3dc0c5300610825.jpg",
            "image_type": "boxart"
        },
        {
            "url": "https://art-s.nflximg.net/22d08/560211126a4cbc0351d4545eee5221f94b022d08.jpg",
            "image_type": "bg"
        },
        {
            "url": "https://art-s.nflximg.net/5fe0f/1e7932a9bbf28adfc52d92fe6f92ef883695fe0f.jpg",
            "image_type": "bo342x684"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABSYKXdtDmOOjabtoc7oF5OUZFbsnZm4526zCL3FYmYp4RDhCv9Mw8m7XS0ym2S1SG375NvilN-LYgk8V-sa21Un-qPx2.jpg?r=e04",
            "image_type": "bg"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/E8vDc_W8CLv7-yMQu8KMEC7Rrr8/AAAABQhaw6ooduaeVRwHI6tkibYxNxrJgmzATkTEOe5_yA6fuIqns8-Dg6rTMKkJn_fp9zVHYPAj9WqOQrlOpvlQdE7KfYUZ.jpg?r=776",
            "image_type": "bg"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABcRDr6fbQ5zoGWrY4qVN7P3paEOOf_sVG1WbrTYzL2KmfWZdAFfReDl_r7y2-PC17h6nUA6PP9D9yIEBRwS5OTI4pQ.jpg?r=a1e",
            "image_type": "bo166x236"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABW8ZgA4rIVS2cOVVFOHnJFAEtN_FesWd0xCSVaoejuTyrKxk5IzGZF-3lGkiS7E0sU05luFuv3yzsMqnk2zzWV8yVept.jpg?r=a1e",
            "image_type": "bo342x684"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/tx1O544a9T7n8Z_G12qaboulQQE/AAAABazJn53SUaBOBxLcVIYTm1zPmsKEUgNoGdDoDVfeuUPtlxUMwrcI0aiM9bx2YR7TWoXOGj2pMdrYjqgkAVUmNvv1BAZwAAzxZA.png?r=c0d",
            "image_type": "bleedback"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABbnCEF0hlRvB-oxUAW-Tfw4VR40pPb1fRNMnN5Vr8GF7UGgJgCrEiCjMf4s8Er5qeSjDxPNpEU6IQJUPBpPyzf9NIa8g.jpg?r=01d",
            "image_type": "bo1280x448"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABUr3Y1-NF-H2vxX46gBEwdYqSlvDsY126karuPPoXnHjijxuk1cXPIb8lrLk8TfN3YXWzniCLhrTOROMXuLaKcji8lI.jpg?r=01d",
            "image_type": "bo342x192"
        },
        {
            "url": "https://occ-0-1068-92.1.nflxso.net/dnm/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAABXu-_LuiAAUXDEgUl0eWjcr09Y3m-r5fwRTtAaCezs6-T9iDACfvGyBC507heeLPEl0hiHqjdX7UF4CY--5Envb_DSmo.jpg?r=01d",
            "image_type": "bo665x375"
        },
        {
            "url": "https://occ-0-1091-299.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABYxZZBmIguwiUza6c-QeBGYe8RYRAj6rs2oKsjWydQ6RZ0gbq7nk0ZQSuVTi-X-outU-CJmhpcMbNNo7IHwLuLvAqA.jpg?r=d2f",
            "image_type": "boxart"
        },
        {
            "url": "https://occ-0-114-116.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAAARPvAntismewdFsimXxpB8fMhloLgSvEQsnnQXSPOCYUDkSO97zaZi4lAt1rN2tj62rmc5l-FBAzBd-grC2BvYskNg.jpg?r=289",
            "image_type": "boxart"
        },
        {
            "url": "https://occ-0-114-116.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABcRDr6fbQ5zoGWrY4qVN7P3paEOOf_sVG1WbrTYzL2KmfWZdAFfReDl_r7y2-PC17h6nUA6PP9D9yIEBRwS5OTI4pQ.jpg?r=a1e",
            "image_type": "boxart"
        },
        {
            "url": "https://occ-0-1223-58.1.nflxso.net/art/f5bad/b9e1e150e3f14118ae2e448f3de1eca757cf5bad.jpg",
            "image_type": "billboard"
        },
        {
            "url": "https://occ-0-1223-58.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABbfYbxKOzCWI7vK76tZ1dL9u7AmOYaK8yAY5hMNocEznGiVxHnAMegpmL1M00tXXVNZwFGRGJFEr4N8d6zdgbc5VU17stYn-Dg.jpg?r=01d",
            "image_type": "bo665x375"
        },
        {
            "url": "https://occ-0-1223-58.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABf-ZUXXm2_L9Pu537uUYHZH5ToOjipdmu7aM3Vwm7555-P_evIEIFyyOZxyS-qd9glX3SiyktBOH9nx4I9tTVjcFqOXwpc8p.jpg?r=01d",
            "image_type": "bo342x192"
        },
        {
            "url": "https://occ-0-1223-58.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABQZtslU0LfgaZ5T4Dt-z-h7H6Z52nCMW_O9GRVqbBs1rn9aR5ojEX7TDCGPRGDi9bTWROmc0LhWWON5k2OU4exEpFAms0VoF7A.jpg?r=01d",
            "image_type": "bo1280x448"
        },
        {
            "url": "https://occ-0-1223-58.1.nflxso.net/dnm/api/v6/XsrytRUxks8BtTRf9HNlZkW2tvY/AAAABVKFiTJZ0umEzQZnJMzHAlUEIjT5HimGxNN-2eXel8da8bpN8i12aCDIEUqQseMupO4iGi7hG-vLo6gO1z6heTZQT9tmfbctCg.jpg?r=a1e",
            "image_type": "bo342x684"
        },
        {
            "url": "https://occ-0-2042-1007.1.nflxso.net/art/21fa8/69a71f6d28ca83423ef8df470f8deb588d221fa8.jpg",
            "image_type": "bg"
        },
        {
            "url": "https://occ-0-2042-1007.1.nflxso.net/art/2287b/672474bcd6d53267f358d520aadc8bcf1012287b.jpg",
            "image_type": "bg"
        },
        {
            "url": "https://occ-0-2773-2774.1.nflxso.net/dnm/api/v6/XsrytRUxks8BtTRf9HNlZkW2tvY/AAAABarsH006nHCKxc8bahwc6_EKG8wUR37yNgaeqXqVmAUMJmuzLgtkfNyDawPN9G9Gtil8j1Pes0pafauu1rM0lwPA2A.jpg?r=d2f",
            "image_type": "boxart"
        },
        {
            "url": "https://occ-0-2773-2774.1.nflxso.net/dnm/api/v6/XsrytRUxks8BtTRf9HNlZkW2tvY/AAAABej-1_2c2BJRatUfbLz85N4RVbmDOqV-IkXCUGAwf6rRxIMOWzocuSj9x4IDzoBdoCxETWTqTQYCMVG8uMA-_A7lGQ.jpg?r=a1e",
            "image_type": "boxart"
        },
        {
            "url": "https://occ-0-3377-185.1.nflxso.net/dnm/api/v6/XsrytRUxks8BtTRf9HNlZkW2tvY/AAAAATQQ0pfPUa-iEgOqw-n--I5VBjUd2q4Vu_GPY9vJXdpAA_foq8K6fUxZTvkZydMmXRxfbiCPgruhkdM5JkkKaDt_Gg.jpg?r=289",
            "image_type": "boxart"
        },
        {
            "url": "https://occ-0-768-769.1.nflxso.net/dnm/api/v6/0DW6CdE4gYtYx8iy3aj8gs9WtXE/AAAABVP3CMkYo3EOr9L-d8E2UFobdUFnmy9zmmlZKBHnOj0zaL3tEKOVaPENZlxPuE3e_i0Za-CUgZPL2ypBKDCM4dKGpiFf.jpg?r=01d",
            "image_type": "bo1280x448"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/34613/a2a03c3d3457c54da30388c7b473b6d04b3b17e8.jpg",
            "image_type": "bo342x192"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/35397/6fa3d8a936f9b8a4703cb1d626e13092a087f95e.jpg",
            "image_type": "bo665x375"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/35437/9db37c324773b29413f445b73c942ae78844ed34.jpg",
            "image_type": "bo1280x448"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/62514/b4c455d961a92716af562429d44d2b1d5c0f92b4.jpg",
            "image_type": "bo342x192"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/62978/dab273a2878e27581f8df048dfe7ccc42dbb2867.jpg",
            "image_type": "bo342x192"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/64319/a23875d1e95594c7d98ca89cd5ef07e9252c2d6f.jpg",
            "image_type": "bo665x375"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/64368/a3675ad701b60ad2ef23ef0838f292f852511a2b.jpg",
            "image_type": "bo1280x448"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/65824/44a481f7ffb0dcd5f6c7db60a490dad5d3456ae0.jpg",
            "image_type": "bo665x375"
        },
        {
            "url": "https://scdn.nflximg.net/ipl/65907/a7f30e951dd07288c45f4c1aa818dba4d52ec907.jpg",
            "image_type": "bo1280x448"
        },
        {
            "url": "https://so-s.nflximg.net/soa2/982/2125954982.jpg",
            "image_type": "bg"
        },
        {
            "url": "https://so-s.nflximg.net/soa4/468/2125974468.jpg",
            "image_type": "bg"
        }
    ]
}