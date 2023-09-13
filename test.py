import os
import sys
import requests
import json
from prettytable import PrettyTable
URL = "https://whatsinmess.vercel.app/api/get_menu"

response = requests.get(URL)
response_json = response.json()


days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

# # 
with open('data.json', 'w') as f:
    json.dump(response_json, f, indent=4)
#
table = PrettyTable(
    
)
meal_names=["Breakfast", "Lunch", "Snacks", "Dinner"]


menu = []
for meals in meal_names:
    menu.append(response_json['data'][0]['wednesday'][meals])

# print(menu)
for i in range(4):
    table.add_column(meal_names[i],menu[i])
    print(table)
    table.clear()
# print(table)