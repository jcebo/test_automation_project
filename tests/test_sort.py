import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TestInventory(unittest.TestCase):
    
    def setUp(self):
        firefox_binary_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        service = Service('C:/test/geckodriver.exe')        
        options = Options()
        options.binary_location = firefox_binary_path
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()

    def tearDown(self):        
        self.driver.quit()

    def test_sort(self):
        login_page = LoginPage(self.driver)                
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        sort_dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("lohi")
        inventory_items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        last_item = inventory_items[-1].text
        self.assertEqual(last_item, "Sauce Labs Fleece Jacket", f"Ostatni produkt nie jest 'Sauce Labs Fleece Jacket', ale {last_item}.")


        
