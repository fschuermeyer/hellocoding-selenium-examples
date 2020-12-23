from selenium import webdriver
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Current Working Directionary auf das Aktuelle Script Setzen

driver = webdriver.Firefox(executable_path='../driver/geckodriver')

driver.maximize_window()

driver.get("https://www.hellocoding.de")
