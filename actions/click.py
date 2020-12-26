from selenium import webdriver
import os

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Firefox(executable_path='../driver/geckodriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")

driver.find_element_by_css_selector('#navigation-handler > ul > li.search.noChildren > a').click()
