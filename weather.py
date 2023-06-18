import json

with open("data.json") as file:
    data = json.load(file)
    temp_data = data['result']['list']

for temp in temp_data:
    if temp['main']["temp_max"] > 30:
        temp_date = temp["dt_txt"].split(":")[0][0:10]
        day_temp = temp["main"]["temp"]
        print(f"{temp_date}: {day_temp}")
