from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
import json
from time import sleep

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Firefox(executable_path='../driver/geckodriver')

driver.maximize_window()

url = "https://hellocoding.de/artikel-idee"

with open('fill.json','r') as file:
    obj = json.loads(file.read())

wait = WebDriverWait(driver, 5)

for data in obj:
    driver.get(url)

    driver.find_element_by_name('Name').send_keys(data['name'])

    driver.find_element_by_name('Thema').send_keys(data['thema'])

    driver.find_element_by_name('Discord Name').send_keys(data['discord'])

    driver.find_element_by_name('sender-mail').send_keys(data['email'])

    driver.find_element_by_name('privacy').click()

    driver.find_element_by_name('anfrage-senden').click()

    try: 
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.form-message-success')))
    except TimeoutException as error:
        driver.quit()

driver.quit()