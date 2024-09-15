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

    def test_inventory_loaded(self):
        login_page = LoginPage(self.driver)
                
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        
        jacket_add_button = self.driver.find_element(By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']/ancestor::div[@class='inventory_item']//button")
        jacket_add_button.click()
        
        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()
        
        jacket_in_cart = self.driver.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Fleece Jacket']")
        self.assertIsNotNone(jacket_in_cart, "Kurtka Sauce Labs Fleece Jacket nie znajduje się w koszyku.")
        
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()

        self.driver.find_element(By.ID, "first-name").send_keys("Jan")
        self.driver.find_element(By.ID, "last-name").send_keys("Kowalski")
        self.driver.find_element(By.ID, "postal-code").send_keys("30-111")
        
        continue_button = self.driver.find_element(By.ID, "continue")
        continue_button.click()
        
        finish_button = self.driver.find_element(By.ID, "finish")
        finish_button.click()

        thank_you_message = self.driver.find_element(By.XPATH, "//h2[text()='Thank you for your order!']")
        self.assertIsNotNone(thank_you_message, "Napis 'Thank you for your order!' nie pojawił się po zakończeniu zamówienia.")

        
