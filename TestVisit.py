import unittest
from selenium import webdriver
import page
import time

class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://barretastic.m3v.us/")

    def test_login_functionality(self):
        reg_page = page.MainPage(self.driver)
        reg_page.click_find_my_plan_header_button()
        first_dropdown = page.MainPage(self.driver)
        first_dropdown.click_first_dropdown()
        pick_a_goal = page.MainPage(self.driver)
        pick_a_goal.pick_goal()
        time.sleep(1)
        second_dropdown = page.MainPage(self.driver)
        second_dropdown.click_second_dropdown()
        pick_a_motivation = page.MainPage(self.driver)
        pick_a_motivation.pick_motivation()
        time.sleep(1)
        third_dropdown = page.MainPage(self.driver)
        third_dropdown.click_third_dropdown()
        pick_amount = page.MainPage(self.driver)
        pick_amount.pick_amount()
        time.sleep(1)
        submit_plan = page.MainPage(self.driver)
        submit_plan.click_find()

    def test_pricing_page(self):
        buy_this_plan = page.PricingPage(self.driver)
        buy_this_plan.click_buy_plan()


        '''main_page = page.MainPage(self.driver)
        main_page.click_login_button()
        user_name = page.LoginPage(self.driver)
        user_name.input_valid_username()
        pass_login = page.LoginPage(self.driver)
        pass_login.input_valid_password()
        login_page = page.LoginPage(self.driver)
        login_page.click_to_login()'''
        #assert main_page.is_title_matches(), "Login"
        #main_page.seacrh_text_element = "BARRETASTIC360"

        #login_page = page.LoginPage(self.driver)

    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()
