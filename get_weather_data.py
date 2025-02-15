import requests


API_KEY = "c4ed19f80c176968f05aa020d9785567"
payload = {
    "q": "bangkok",
    "appid": API_KEY,
    "units": "metric"
}
url = "https://api.openweathermap.org/data/2.5/weather"
response = requests.get(url, params=payload)
print(response.url)

data = response.json()
print(data)