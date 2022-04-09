# Code Snippets

import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
    'x-rapidapi-key': "8c3ee30dfcmsh1b2042bd6f9f5e1p1fcd92jsn6ffac72ad451"
    }

conn.request("GET", "/title/countries?netflix_id=70143836", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

# Results

{
  "Object": {
      "total": 37,
      "limit": 100,
      "offset": 0
  },
  "results": [
      {
          "country_code": "AR",
          "country": "Argentina ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English [Original],Spanish,Brazilian Portuguese,English - Audio Description",
          "subtitle": "Spanish,Brazilian Portuguese,English"
      },
      {
          "country_code": "BE",
          "country": "Belgium ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English - Audio Description,English [Original],French",
          "subtitle": "English,French,Dutch"
      },
      {
          "country_code": "BR",
          "country": "Brazil ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English [Original],Spanish,Brazilian Portuguese",
          "subtitle": "Spanish,Brazilian Portuguese"
      },
      {
          "country_code": "CA",
          "country": "Canada ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English - Audio Description,English [Original]",
          "subtitle": "English"
      },
      {
          "country_code": "CO",
          "country": "Colombia ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2021-01-12",
          "audio": "English [Original],Spanish",
          "subtitle": "Spanish"
      },
      {
          "country_code": "CZ",
          "country": "Czech Republic ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "German,English - Audio Description,English [Original],Polish,Spanish,French",
          "subtitle": "Czech,German,English,Polish,Spanish,French"
      },
      {
          "country_code": "FR",
          "country": "France ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English - Audio Description,English [Original],French",
          "subtitle": "English,French"
      },
      {
          "country_code": "DE",
          "country": "Germany ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "German,English - Audio Description,English [Original],French,Spanish",
          "subtitle": "German,English,French,Spanish"
      },
      {
          "country_code": "GR",
          "country": "Greece ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-06",
          "audio": "German,English - Audio Description,English [Original],French,Turkish,Spanish",
          "subtitle": "German,Greek,English,French,Turkish,Spanish"
      },
      {
          "country_code": "HK",
          "country": "Hong Kong ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-09",
          "audio": "English - Audio Description,English [Original],Japanese",
          "subtitle": "British English,English,Simplified Chinese,Traditional Chinese"
      },
      {
          "country_code": "HU",
          "country": "Hungary ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2019-08-08",
          "audio": "German,English - Audio Description,English [Original],French",
          "subtitle": "German,English,French,Hungarian,Romanian"
      },
      {
          "country_code": "IS",
          "country": "Iceland ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "English - Audio Description,English [Original],Spanish",
          "subtitle": "Danish,English,Spanish"
      },
      {
          "country_code": "IN",
          "country": "India ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-09",
          "audio": "English - Audio Description,English [Original],Spanish,Brazilian Portuguese",
          "subtitle": "British English,English,Spanish,Brazilian Portuguese"
      },
      {
          "country_code": "IL",
          "country": "Israel ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "English - Audio Description,English [Original],Polish",
          "subtitle": "Arabic,British English,English,Hebrew,Russian,Romanian"
      },
      {
          "country_code": "IT",
          "country": "Italy ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2019-06-14",
          "audio": "German,English - Audio Description,English [Original],European Spanish,French,Italian,Spanish",
          "subtitle": "German,Greek,English,French,Italian,Romanian,Spanish"
      },
      {
          "country_code": "JP",
          "country": "Japan ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2018-09-15",
          "audio": "English - Audio Description,English [Original],Japanese",
          "subtitle": "English,Japanese"
      },
      {
          "country_code": "LT",
          "country": "Lithuania ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "German,English - Audio Description,English [Original]",
          "subtitle": "German,English,Russian"
      },
      {
          "country_code": "MY",
          "country": "Malaysia ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2020-11-30",
          "audio": "English - Audio Description,English [Original],Japanese,Spanish",
          "subtitle": "British English,English,Simplified Chinese,Traditional Chinese,Spanish"
      },
      {
          "country_code": "MX",
          "country": "Mexico ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English [Original],Spanish,English - Audio Description",
          "subtitle": "Spanish,English"
      },
      {
          "country_code": "NL",
          "country": "Netherlands ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-15",
          "audio": "German,English - Audio Description,English [Original],French",
          "subtitle": "German,English,French,Dutch"
      },
      {
          "country_code": "PH",
          "country": "Philippines ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2021-04-12",
          "audio": "English - Audio Description,English [Original],Spanish,Japanese",
          "subtitle": "British English,English,Spanish,Simplified Chinese,Traditional Chinese"
      },
      {
          "country_code": "PL",
          "country": "Poland ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "German,English - Audio Description,English [Original],Polish,Spanish",
          "subtitle": "German,English,Polish,Russian,Spanish"
      },
      {
          "country_code": "PT",
          "country": "Portugal ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-06",
          "audio": "English - Audio Description,English [Original],European Spanish,French,Brazilian Portuguese",
          "subtitle": "English,European Spanish,French,Portuguese"
      },
      {
          "country_code": "RO",
          "country": "Romania ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "German,English - Audio Description,English [Original],European Spanish,French,Polish,Turkish",
          "subtitle": "German,English,European Spanish,French,Hungarian,Romanian"
      },
      {
          "country_code": "RU",
          "country": "Russia",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-03-01",
          "audio": "German,English - Audio Description,English [Original],French,Polish,Turkish",
          "subtitle": "German,British English,English,French,Russian,Finnish,Hungarian,Polish,Romanian,Turkish"
      },
      {
          "country_code": "SG",
          "country": "Singapore ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-09",
          "audio": "English - Audio Description,English [Original],Japanese,Spanish",
          "subtitle": "British English,English,Simplified Chinese,Traditional Chinese,Spanish"
      },
      {
          "country_code": "SK",
          "country": "Slovakia ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "German,English - Audio Description,English [Original],Polish,Spanish,French",
          "subtitle": "Czech,German,English,Hungarian,Polish,Spanish,French"
      },
      {
          "country_code": "ZA",
          "country": "South Africa",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-03-01",
          "audio": "English - Audio Description,English [Original]",
          "subtitle": "British English,English"
      },
      {
          "country_code": "KR",
          "country": "South Korea",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-09",
          "audio": "English - Audio Description,English [Original],Japanese",
          "subtitle": "British English,English,Korean"
      },
      {
          "country_code": "ES",
          "country": "Spain ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-06",
          "audio": "German,English - Audio Description,English [Original],European Spanish,French,Italian,Spanish",
          "subtitle": "Arabic,English,European Spanish,French,Romanian,Spanish"
      },
      {
          "country_code": "SE",
          "country": "Sweden ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "English - Audio Description,English [Original],Spanish",
          "subtitle": "Danish,English,Finnish,Norwegian,Swedish,Spanish"
      },
      {
          "country_code": "CH",
          "country": "Switzerland ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-14",
          "audio": "German,English - Audio Description,English [Original],French,Italian,Brazilian Portuguese",
          "subtitle": "German,English,French,Italian,Portuguese"
      },
      {
          "country_code": "TH",
          "country": "Thailand ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2019-06-29",
          "audio": "English - Audio Description,English [Original],Japanese",
          "subtitle": "British English,English,Thai,Simplified Chinese,Traditional Chinese"
      },
      {
          "country_code": "TR",
          "country": "Turkey ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2016-01-07",
          "audio": "English - Audio Description,English [Original],Turkish,Spanish,German,French",
          "subtitle": "Arabic,Greek,English,Turkish,Spanish,German,French,Dutch"
      },
      {
          "country_code": "UA",
          "country": "Ukraine ",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2021-05-27",
          "audio": "English - Audio Description,English [Original],Polish,Turkish",
          "subtitle": "British English,English,Polish,Romanian,Russian,Turkish"
      },
      {
          "country_code": "GB",
          "country": "United Kingdom",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2015-04-15",
          "audio": "English - Audio Description,English [Original]",
          "subtitle": "English"
      },
      {
          "country_code": "US",
          "country": "United States",
          "season_detail": "S1:7,S2:13,S3:13,S4:13,S5:16",
          "expire_date": "",
          "new_date": "2021-07-15",
          "audio": "English - Audio Description,English [Original],Spanish",
          "subtitle": "English,Spanish"
      }
  ]
}