from selenium import webdriver
import os

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

options = webdriver.firefox.options.Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options,executable_path='../driver/geckodriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")

print(driver.find_element_by_css_selector('html body h1').get_attribute('innerHTML'))

driver.quit()