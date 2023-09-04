import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import prettytable

SKIP_DAYS = 4
NO_OF_NEXT_CLICKS = 27

driver = webdriver.Firefox()
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
next_button = driver.find_element(By.ID, "next")
prev_button = driver.find_element(By.ID, "previous")
day = driver.find_element(By.ID, "day").get_attribute("innerHTML")
# day = "Tuesday"
# print(days[day]) #output is 2

#interating through breakfast

