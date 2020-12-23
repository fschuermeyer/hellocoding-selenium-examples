from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Safari()

wait = WebDriverWait(driver, 5)

driver.maximize_window()

driver.get("https://www.google.de")

sleep(5)

privacyiFrame = driver.find_elements_by_css_selector('iframe')

if privacyiFrame:
    driver.switch_to.frame(0)
    driver.find_element_by_id('introAgreeButton').click()

driver.switch_to.parent_frame()

element = driver.find_element_by_name('q')

element.send_keys('Google with Safari Automatisation')

element.send_keys(Keys.RETURN)

failed = False

try: 
   element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search')))
   search_results = element.find_elements_by_css_selector('.g')
except TimeoutException as error:
    failed = True

if failed != True:

    titles = []

    for search_item in search_results:
        try:
            item = WebDriverWait(search_item, 5) 

            title_elm = item.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3 > span')))

            titles.append(title_elm.get_attribute('innerHTML'))
        except TimeoutException as error:
            pass

driver.quit()

print(titles) 
