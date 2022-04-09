#Code Snippets

import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "8c3ee30dfcmsh1b2042bd6f9f5e1p1fcd92jsn6ffac72ad451"
    }

conn.request("GET", "/static/countries", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Results

{
    "results": [
        {
            "id": 21,
            "country": "Argentina ",
            "countrycode": "AR",
            "expiring": 56,
            "nl7": 68,
            "tvids": 5695,
            "tmovs": 3723,
            "tseries": 1972
        },
        {
            "id": 23,
            "country": "Australia ",
            "countrycode": "AU",
            "expiring": 85,
            "nl7": 46,
            "tvids": 6072,
            "tmovs": 3870,
            "tseries": 2202
        },
        {
            "id": 26,
            "country": "Belgium ",
            "countrycode": "BE",
            "expiring": 63,
            "nl7": 62,
            "tvids": 6188,
            "tmovs": 4131,
            "tseries": 2057
        },
        {
            "id": 29,
            "country": "Brazil ",
            "countrycode": "BR",
            "expiring": 58,
            "nl7": 71,
            "tvids": 5750,
            "tmovs": 3778,
            "tseries": 1972
        },
        {
            "id": 33,
            "country": "Canada ",
            "countrycode": "CA",
            "expiring": 68,
            "nl7": 74,
            "tvids": 6062,
            "tmovs": 3970,
            "tseries": 2092
        },
        {
            "id": 36,
            "country": "Colombia ",
            "countrycode": "CO",
            "expiring": 56,
            "nl7": 68,
            "tvids": 5485,
            "tmovs": 3519,
            "tseries": 1966
        },
        {
            "id": 307,
            "country": "Czech Republic ",
            "countrycode": "CZ",
            "expiring": 66,
            "nl7": 86,
            "tvids": 7359,
            "tmovs": 5268,
            "tseries": 2091
        },
        {
            "id": 45,
            "country": "France ",
            "countrycode": "FR",
            "expiring": 47,
            "nl7": 58,
            "tvids": 5914,
            "tmovs": 3888,
            "tseries": 2026
        },
        {
            "id": 39,
            "country": "Germany ",
            "countrycode": "DE",
            "expiring": 61,
            "nl7": 80,
            "tvids": 6662,
            "tmovs": 4558,
            "tseries": 2104
        },
        {
            "id": 327,
            "country": "Greece ",
            "countrycode": "GR",
            "expiring": 58,
            "nl7": 74,
            "tvids": 6204,
            "tmovs": 4212,
            "tseries": 1992
        },
        {
            "id": 331,
            "country": "Hong Kong ",
            "countrycode": "HK",
            "expiring": 61,
            "nl7": 42,
            "tvids": 5609,
            "tmovs": 3498,
            "tseries": 2111
        },
        {
            "id": 334,
            "country": "Hungary ",
            "countrycode": "HU",
            "expiring": 69,
            "nl7": 64,
            "tvids": 6897,
            "tmovs": 4815,
            "tseries": 2082
        },
        {
            "id": 265,
            "country": "Iceland ",
            "countrycode": "IS",
            "expiring": 63,
            "nl7": 74,
            "tvids": 6244,
            "tmovs": 4175,
            "tseries": 2069
        },
        {
            "id": 337,
            "country": "India ",
            "countrycode": "IN",
            "expiring": 68,
            "nl7": 41,
            "tvids": 5919,
            "tmovs": 3655,
            "tseries": 2264
        },
        {
            "id": 336,
            "country": "Israel ",
            "countrycode": "IL",
            "expiring": 78,
            "nl7": 52,
            "tvids": 5715,
            "tmovs": 3651,
            "tseries": 2064
        },
        {
            "id": 269,
            "country": "Italy ",
            "countrycode": "IT",
            "expiring": 45,
            "nl7": 79,
            "tvids": 5992,
            "tmovs": 4018,
            "tseries": 1974
        },
        {
            "id": 267,
            "country": "Japan ",
            "countrycode": "JP",
            "expiring": 76,
            "nl7": 75,
            "tvids": 6610,
            "tmovs": 4190,
            "tseries": 2420
        },
        {
            "id": 357,
            "country": "Lithuania ",
            "countrycode": "LT",
            "expiring": 66,
            "nl7": 72,
            "tvids": 6370,
            "tmovs": 4286,
            "tseries": 2084
        },
        {
            "id": 378,
            "country": "Malaysia ",
            "countrycode": "MY",
            "expiring": 69,
            "nl7": 41,
            "tvids": 5955,
            "tmovs": 3569,
            "tseries": 2386
        },
        {
            "id": 65,
            "country": "Mexico ",
            "countrycode": "MX",
            "expiring": 55,
            "nl7": 68,
            "tvids": 5762,
            "tmovs": 3792,
            "tseries": 1970
        },
        {
            "id": 67,
            "country": "Netherlands ",
            "countrycode": "NL",
            "expiring": 53,
            "nl7": 94,
            "tvids": 6309,
            "tmovs": 4305,
            "tseries": 2004
        },
        {
            "id": 390,
            "country": "Philippines ",
            "countrycode": "PH",
            "expiring": 61,
            "nl7": 43,
            "tvids": 5778,
            "tmovs": 3426,
            "tseries": 2352
        },
        {
            "id": 392,
            "country": "Poland ",
            "countrycode": "PL",
            "expiring": 43,
            "nl7": 55,
            "tvids": 5953,
            "tmovs": 4010,
            "tseries": 1943
        },
        {
            "id": 268,
            "country": "Portugal ",
            "countrycode": "PT",
            "expiring": 47,
            "nl7": 84,
            "tvids": 6000,
            "tmovs": 4035,
            "tseries": 1965
        },
        {
            "id": 400,
            "country": "Romania ",
            "countrycode": "RO",
            "expiring": 79,
            "nl7": 74,
            "tvids": 6370,
            "tmovs": 4360,
            "tseries": 2010
        },
        {
            "id": 402,
            "country": "Russia",
            "countrycode": "RU",
            "expiring": 65,
            "nl7": 38,
            "tvids": 5710,
            "tmovs": 3624,
            "tseries": 2086
        },
        {
            "id": 408,
            "country": "Singapore ",
            "countrycode": "SG",
            "expiring": 63,
            "nl7": 52,
            "tvids": 6317,
            "tmovs": 3951,
            "tseries": 2366
        },
        {
            "id": 412,
            "country": "Slovakia ",
            "countrycode": "SK",
            "expiring": 66,
            "nl7": 65,
            "tvids": 6471,
            "tmovs": 4375,
            "tseries": 2096
        },
        {
            "id": 447,
            "country": "South Africa",
            "countrycode": "ZA",
            "expiring": 64,
            "nl7": 44,
            "tvids": 5887,
            "tmovs": 3709,
            "tseries": 2178
        },
        {
            "id": 348,
            "country": "South Korea",
            "countrycode": "KR",
            "expiring": 65,
            "nl7": 45,
            "tvids": 5384,
            "tmovs": 3383,
            "tseries": 2001
        },
        {
            "id": 270,
            "country": "Spain ",
            "countrycode": "ES",
            "expiring": 52,
            "nl7": 72,
            "tvids": 6089,
            "tmovs": 4097,
            "tseries": 1992
        },
        {
            "id": 73,
            "country": "Sweden ",
            "countrycode": "SE",
            "expiring": 53,
            "nl7": 68,
            "tvids": 5622,
            "tmovs": 3691,
            "tseries": 1931
        },
        {
            "id": 34,
            "country": "Switzerland ",
            "countrycode": "CH",
            "expiring": 70,
            "nl7": 62,
            "tvids": 6193,
            "tmovs": 4026,
            "tseries": 2167
        },
        {
            "id": 425,
            "country": "Thailand ",
            "countrycode": "TH",
            "expiring": 60,
            "nl7": 50,
            "tvids": 6226,
            "tmovs": 3888,
            "tseries": 2338
        },
        {
            "id": 432,
            "country": "Turkey ",
            "countrycode": "TR",
            "expiring": 56,
            "nl7": 44,
            "tvids": 5619,
            "tmovs": 3656,
            "tseries": 1963
        },
        {
            "id": 436,
            "country": "Ukraine ",
            "countrycode": "UA",
            "expiring": 66,
            "nl7": 41,
            "tvids": 5339,
            "tmovs": 3264,
            "tseries": 2075
        },
        {
            "id": 46,
            "country": "United Kingdom",
            "countrycode": "GB",
            "expiring": 86,
            "nl7": 58,
            "tvids": 6497,
            "tmovs": 4223,
            "tseries": 2274
        },
        {
            "id": 78,
            "country": "United States",
            "countrycode": "US",
            "expiring": 70,
            "nl7": 59,
            "tvids": 5911,
            "tmovs": 3784,
            "tseries": 2127
        }
    ]
}