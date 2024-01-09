import calendar
import datetime
import requests
import json
from prettytable import PrettyTable
import os
from pathlib import Path

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
    "Sunday": 6,
}
data_path = Path("wt_mess/data/")
if data_path.is_dir():
    pass
    # print('alre there')
else:
    data_path.mkdir(parents=True, exist_ok=True)
    with open(data_path / "data.json", "w") as f:
        json.dump(response_json, f, indent=4)
# if data.json.is_file()

#
table = PrettyTable()


def meal_name() -> str:
    current_time = datetime.datetime.now().time()
    breakfast_end_time = datetime.time(hour=9, minute=00)
    lunch_end_time = datetime.time(hour=13, minute=00)
    snacks_end_time = datetime.time(hour=17, minute=30)
    dinner_end_time = datetime.time(hour=21, minute=00)
    if breakfast_end_time > current_time:
        return "Breakfast"
    elif lunch_end_time > current_time:
        return "Lunch"
    elif snacks_end_time > current_time:
        return "Snacks"
    else:
        return "Dinner"


meal = meal_name()
# meal_names=["Breakfast", "Lunch", "Snacks", "Dinner"]
current_date = datetime.datetime.now().date()
day_name = calendar.day_name[current_date.weekday()].lower()
current_time = datetime.datetime.now().time()

menu = []
# for meals in meal_names:
menu.append(response_json["data"][0][day_name][meal])

# print(menu)
# for i in range(4):

print(f"\n{current_date} | {day_name} | {current_time}")

table.add_column(meal, menu[0])
print(table)
# table.clear()
# # print(table)
