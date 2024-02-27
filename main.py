import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# params
# booking dates 30 May - 2 June
url = "https://www.travelyosemite.com/lodging/housekeeping-camp"
options = Options()
# options.add_argument("--headless")
arrival_input_id = "container-widget-hero_ArrivalDate"
arrival_date = "5/30/2024"
depart_date = "6/2/2024"


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)
driver.get(url)

# sleep 10 sec (until page elements load)
sleep(5)

arrival_input_element = driver.find_element(By.ID, arrival_input_id)
print(arrival_input_element.get_attribute("name"))
# arrival_input_element.send_keys(arrival_date)
