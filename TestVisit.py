import unittest
from selenium import webdriver
import page

class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://barretastic.m3v.us/")

    def test_login_functionality(self):
        main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        user_name = page.LoginPage(self.driver)
        user_name.input_valid_username()
        pass_login = page.LoginPage(self.driver)
        pass_login.input_valid_password()
        login_page = page.LoginPage(self.driver)
        login_page.click_to_login()
        #assert main_page.is_title_matches(), "Login"
        #main_page.seacrh_text_element = "BARRETASTIC360"

        #login_page = page.LoginPage(self.driver)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
