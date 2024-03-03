import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

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
depart_input_id = "container-widget-hero_DepartureDate"
depart_date = "6/2/2024"
submit_button_name = "wxa-form-button-submit"
xpath = "/html/body/div[9]/div/div/div/div[2]/div[2]/div/form/div[10]/input"

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

driver.get(url)

arrival_input_element = driver.find_element(By.ID, arrival_input_id)
arrival_input_element.clear()
arrival_input_element.send_keys(arrival_date)

depart_input_element = driver.find_element(By.ID, depart_input_id)
depart_input_element.clear()
depart_input_element.send_keys(depart_date)

# sleep(5)
submit_button_element = driver.find_element(By.XPATH, xpath)
print("button: ", submit_button_element.get_attribute("value"))
# action = ActionChains(driver)
# action.move_to_element(submit_button_element)
# action.click(submit_button_element)
submit_button_element.click()

sleep(5)
# submit_button_element.click()
no_results = "box-results-empty-outer"

try:
    no_results_element = driver.find_element(By.ID, no_results)
    print("no results: ", no_results)
except Exception:
    sleep(5)
    heading = driver.find_element(By.TAG_NAME, "h3")
    print("h3: ", heading.get_attribute("innerHTML"))
