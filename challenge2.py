import unittest, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        self.driver.maximize_window()
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.click()
        searchfield.send_keys("exotics")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-lightblue").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "serverSideDataTable_wrapper")))
        target_text = re.search(r'PORSCHE', self.driver.page_source)
        self.assertNotEqual(target_text, None)


if __name__ == '__main__':
    unittest.main()