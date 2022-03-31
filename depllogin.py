import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class DeeplTranslate(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Ksusha\Documents\chromedriver.exe")

    def test_login_in_deepl_org(self):
        driver = self.driver
        driver.get('https://www.deepl.com/translator')
        elem_login = driver.find_element(by=By.XPATH, value='/html/body/header/nav/div/div[3]/div[1]/button')
        ActionChains(driver).move_to_element(elem_login)
        driver.find_element(by=By.XPATH, value='/html/body/header/nav/div/div[3]/div[1]/button').click()


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
