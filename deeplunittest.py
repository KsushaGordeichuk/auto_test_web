import unittest
from selenium import webdriver)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class DeeplTranslate(unittest.TestCase): 
    def setUp(self): 
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")

    def test_title_in_deepl_org(self): 
        driver = self.driver
        driver.get('https://www.deepl.com/translator')
        self.assertIn("DeepL", driver.title)
        elem = driver.find_element(by=By.XPATH, value='//*[@id="panelTranslateText"]/div[3]/section[1]/div[3]/div[2]/textarea')
        elem.send_keys("depl")
        assertNotIn("No results found.",  driver.page_source)
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()

