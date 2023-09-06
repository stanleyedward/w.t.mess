import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import prettytable

MEALS_PER_DAY = 4
TOTAL_PAGES = 28 #7*4

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.get("https://whatsinmess.netlify.app/")


days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

meal = {
    "Breakfast": 0,
    "Lunch": 1,
    "Snacks": 2,
    "Dinner": 3
}

next_button = driver.find_element(By.ID, "next")
prev_button = driver.find_element(By.ID, "previous")
day = driver.find_element(By.ID, "day").get_attribute("innerHTML")
# day = "Tuesday"
# print(days[day]) #output is 2

#iteration to get to Monday-breakfast

current_meal = driver.find_element(By.ID,"header").get_attribute("innerHTML")   
current_day = driver.find_element(By.ID, "day").get_attribute("innerHTML")

no_of_prev = (days[current_day])*MEALS_PER_DAY + meal[current_meal]
for i in range(no_of_prev):
    prev_button.click()

#getting breakfast dataset
breakfast = [[]]
for i in range(len(days)):
    dishes = driver.find_elements(By.CLASS_NAME,'list-group-item')
    breakfast.append(dishes)
    for j in range(len(meal)):
            next_button.click()

#getting lunch dataset
lunch = [[]]
next_button.click()
for i in range(len(days)):
    dishes = driver.find_elements(By.CLASS_NAME,'list-group-item')
    lunch.append(dishes)
    for j in range(len(meal)):
            next_button.click()
#getting snacks
snacks = [[]]
next_button.click()
next_button.click()
for i in range(len(days)):
    dishes = driver.find_elements(By.CLASS_NAME,'list-group-item')
    snacks.append(dishes)
    for j in range(len(meal)):
            next_button.click()
#getting dinner
dinner = [[]]
next_button.click()
next_button.click()
next_button.click()
for i in range(len(days)):
    dishes = driver.find_elements(By.CLASS_NAME,'list-group-item')
    dinner.append(dishes)
    for j in range(len(meal)):
            next_button.click()   

#try making an algo to get all 4 datasets from a single nested loop
# breakfast, lunch, snacks, dinner = [[]]
# for i in range(len(days)):
#       for j in range(len(meal)):
#             pass

table = prettytable(
      
      )



