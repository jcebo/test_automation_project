import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    
    def setUp(self):
        firefox_binary_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
        service = Service('C:/test/geckodriver.exe')        
        options = Options()
        options.binary_location = firefox_binary_path
        self.driver = webdriver.Firefox(service=service, options=options)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)        
        login_page.open()
        login_page.login("standard_user", "secret_sauce")
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "title").text == "Products")






