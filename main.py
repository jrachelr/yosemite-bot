import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

lets_go = True

while lets_go == True:
    browser = webdriver.Chrome()
    browser.get("https://www.travelyosemite.com/lodging/housekeeping-camp")
