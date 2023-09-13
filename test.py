import os
import sys
import requests
import json
from prettytable import PrettyTable
URL = "https://whatsinmess.vercel.app/api/get_menu"

response = requests.get(URL)
response_json = response.json()

meal = {
    "Breakfast": 0,
    "Lunch": 1,
    "Snacks": 2,
    "Dinner": 3
}

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
    field_names=["Break","Lunch", "snack", "diner"]
)


menu = []
for meals in meal:
    menu.append(response_json['data'][0]['wednesday'][meals])
# print(menu)

# table.add_rows(menu)
# print(table)
# print(len(menu))
table.add_row(menu[1],)

print(table)