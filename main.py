import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import prettytable

MEALS_PER_DAY = 4
TOTAL_CLICKS = 27

driver = webdriver.Firefox()
driver.implicitly_wait(15)
driver.get("https://whatsinmess.netlify.app/")


days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday":5,
    "Saturday":6,
    "Sunday":7
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

no_of_prev = (days[current_day]-1)*MEALS_PER_DAY + meal[current_meal]
for i in range(no_of_prev):
    prev_button.click()


