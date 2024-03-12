import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from time import sleep
import requests

load_dotenv()


# params
# booking dates 30 May - 2 June
url = "https://www.travelyosemite.com/lodging/housekeeping-camp"
options = Options()
# options.add_argument("--headless")
arrival_input_id = "container-widget-hero_ArrivalDate"
depart_input_id = "container-widget-hero_DepartureDate"
arrival_date = "5/30/2024"
depart_date = "6/2/2024"

# test  dates_available = True
# arrival_date = "4/22/2024"
# depart_date = "4/23/2024"

submit_button_xpath = (
    "/html/body/div[9]/div/div/div/div[2]/div[2]/div/form/div[10]/input"
)
avail_dates_xpath = "/html/body/div[2]/div/div[3]/div/div[2]/div[1]/div/h4[2]"
BOT_API_KEY = os.environ.get("BOT_API_KEY")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def check_availability():
    dates_available = False

    # access search page
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(url)

    # input arrival date
    arrival_input_element = driver.find_element(By.ID, arrival_input_id)
    arrival_input_element.clear()
    arrival_input_element.send_keys(arrival_date)

    # input depart date
    depart_input_element = driver.find_element(By.ID, depart_input_id)
    depart_input_element.clear()
    depart_input_element.send_keys(depart_date)

    # submit form
    submit_button_element = driver.find_element(By.XPATH, submit_button_xpath)
    submit_button_element.click()
    sleep(5)

    wait = WebDriverWait(driver, timeout=5)

    try:
        avail_dates_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, avail_dates_xpath))
        )
        avail_dates_string = avail_dates_element.get_attribute("innerHTML")
        print("avail dates: ", avail_dates_string)
        dates_available = True
        return dates_available

    except Exception:
        no_results_id = "box-results-empty-outer"
        no_results_element = driver.find_element(By.ID, no_results_id)
        no_results_string = no_results_element.get_attribute("innerHTML")
        print("no results: ", no_results_string)
        return dates_available


def send_message(url):
    dates_available = check_availability()

    if dates_available:
        message = f"Housekeeping Camp has availability!! \n book now: {url}"
        telegram_message_url = f"https://api.telegram.org/bot{BOT_API_KEY}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}"
        print(requests.get(telegram_message_url).json())
    else:
        print("dates not available")


send_message(url)
