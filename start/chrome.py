from selenium import webdriver
import os

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path='../driver/chromedriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")
