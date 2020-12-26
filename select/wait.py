from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import os

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path='../driver/chromedriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")

try:
    wait = WebDriverWait(driver, 1)

    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#CookieSettings > div > div > div > div > a')))

    element.click()
except TimeoutException as error:
    failed = True

driver.quit()

if failed:
    print("Element nicht gefudnen!")