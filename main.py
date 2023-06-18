import requests
from data import write_to_file

# https://one-api.ir/weather/?token={token}&action=current&city={city}

URL = "https://one-api.ir/weather/"

parameters = {

    "token": "343451:648e0cc239601",
    "action": "hourly",
    "city": "تهران",
}

response = requests.get(URL, params=parameters)
datax = response.json()

day_list = datax['result']['list']

print(day_list["weather"])
  
