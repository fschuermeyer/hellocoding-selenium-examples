from selenium import webdriver
import os

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Firefox(executable_path='../driver/geckodriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")

location = driver.execute_script("return window.location")

print(location)

print(location['host'])