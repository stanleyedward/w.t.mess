import os
from selenium import webdriver
import prettytable

driver = webdriver.Firefox()
driver.get("https://whatsinmess.netlify.app/")