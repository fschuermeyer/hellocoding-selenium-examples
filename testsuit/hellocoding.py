# Imports für die Test
import unittest
import HtmlTestRunner
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Current Working Directory auf den Pfad des aktuellen Skripts setzen
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class HelloCodingTestSuit(unittest.TestCase):
    baseUrl= "https://hellocoding.de"
    sitemapUrl = "https://www.hellocoding.de/sitemap"

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='../driver/chromedriver')    
        self.driver.maximize_window()
   
        self.driver.implicitly_wait(5) 

    # Homepage Laden
    def test_loading_website(self):        
        self.driver.get(self.baseUrl)        
        # Test ob die Korrekte Webseite Geladen wurde
        self.assertIn("Übersicht, Programmieren Lernen | HelloCoding",self.driver.title)
    
    # Testen ob eine Seite einen 500er Fehler hat
    def test_no_error(self):
        self.driver.get(self.sitemapUrl) 
        failed = True

        wait = WebDriverWait(self.driver, 5)
        # Alle Links aus der Sitemap Holen
        try:
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#contentTOC')))
            elements = element.find_elements_by_css_selector('.sitemap-widget ul li a')
        except TimeoutException as error:
            pass

        if len(elements) != 0: 
            links = []
            for a in elements:
                links.append(a.get_attribute('href'))

            # Jeden Link Prüfen das kein 500er Fehler im Page Source steht. 
            for link in links:
                if link != "":
                    self.driver.get(link)

                    if "500er - Server Fehler" in self.driver.page_source:
                        self.fail(link + " - 500er Fehler")
        else:
            self.fail('Keine Elemente Gefunden')

    # Abschließende Bedingung
    def tearDown(self):
        # Browser Schließen
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./report'))
