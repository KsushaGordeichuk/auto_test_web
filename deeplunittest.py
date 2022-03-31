import unittest
from selenium import webdriver
#driver = webdriver.Chrome(executable_path = "<C:\Users\Ksusha\Documents\chromedriver.exe>")
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#класс кeys обеспечивает взаимодействие с командами клавиатуры
class DeeplTranslate(unittest.TestCase): #наследование класса TestCase -это способ сообщения модулю unittest, что это тест
    def setUp(self): #часть инициализации
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Ksusha\Documents\chromedriver.exe")

    def test_title_in_deepl_org(self): #метод теста всегда должен начинаться с test
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

