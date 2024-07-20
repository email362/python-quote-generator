import requests

url = "http://api.forismatic.com/api/1.0/"
params = {
    "method": "getQuote",
    "format": "json",
    "lang": "en"
}


# print("Quote Text: " + quote["quoteText"])
# print("Author: " + quote["quoteAuthor"])

def getQuote():
    response = requests.get(url, params=params)
    quote = response.json()
    return quote

for i in range(4):
    x = getQuote()
    print(x)

