import json

temp_date_com = []

with open("data.json") as file:
    data = json.load(file)
    temp_data = data['result']['list']

for temp in temp_data:
    if temp['main']["temp_max"] > 20:
        temp_date = temp["dt_txt"].split(":")[0][0:10]
        day_temp = temp["main"]["temp"]
        temp_date_com.append({temp_date: day_temp})

print(temp_date_com)
