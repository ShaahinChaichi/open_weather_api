import requests

API_KEY = "c4bd24d75f7f431ca448b03ab4755bbc"

# https://newsapi.org/v2/everything?q=tesla&from=2023-05-18&sortBy=publishedAt&apiKey=c4bd24d75f7f431ca448b03ab4755bbc
# ?q=tesla&from=2023-05-18&sortBy=publishedAt&apiKey=


URL = "https://newsapi.org/v2/everything"

parameters = {

    "apikey": API_KEY,
    "sortBy": "publishedAt",
    "from": "2023-05-18",
    "q": "tesla"
}

response = requests.get(URL, params=parameters)
data = response.json()
articles = data["articles"]

index = 1
for article in articles:
    print(f'{index}: {article["title"]}')
    index += 1
