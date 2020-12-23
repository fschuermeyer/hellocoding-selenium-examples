from selenium import webdriver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Current Working Directionary auf das Aktuelle Script Setzen

driver = webdriver.Chrome(executable_path='../driver/chromedriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")

print(driver.find_element_by_xpath('.//html//body//h1').get_attribute('innerHTML'))

print(driver.find_element_by_xpath('.//html//body//p').get_attribute('innerHTML'))

driver.quit()