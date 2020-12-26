from selenium import webdriver
import os
from time import sleep
from slugify import slugify

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

driver = webdriver.Chrome(executable_path='../driver/chromedriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de/sitemap")

sleep(4)

elements = driver.find_elements_by_css_selector('#contentTOC .sitemap-widget ul li a')

links = []
for a in elements:
    links.append(a.get_attribute('href'))


for link in links:
    driver.get(link)
    sleep(2)
    driver.save_screenshot('../screenshot-example/' + slugify(link) + '.png')

driver.quit()