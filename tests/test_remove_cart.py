import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


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

    def test_remove_cart(self):
        login_page = LoginPage(self.driver)                
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Bike Light']").click()
        self.driver.find_element(By.ID, "add-to-cart").click()
        self.driver.find_element(By.ID, "remove").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Bike Light']")
        self.assertEqual(len(cart_items), 0, "Produkt 'Sauce Labs Bike Light' jest nadal w koszyku.")

        
