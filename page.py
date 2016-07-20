from element import BasePageElement
from locators import MainPageLocators, SecondPageLocators, PricingPageLocators

class SearchTextElement(BasePageElement):

    locator = "Login"

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Login" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def click_find_my_plan_header_button(self):
        click_js_plan = self.driver.find_element(*MainPageLocators.FIND_MY_PLAN_JS)
        click_js_plan.click()

    def click_first_dropdown(self):
        click_goal = self.driver.find_element(*MainPageLocators.GOAL_DROPDOWN)
        click_goal.click()

    def pick_goal(self):
        pick_one_goal = self.driver.find_element(*MainPageLocators.GOAL)
        pick_one_goal.click()

    def click_second_dropdown(self):
        click_motivation = self.driver.find_element(*MainPageLocators.MOTIVATION_DROPDOWN)
        click_motivation.click()

    def pick_motivation(self):
        pick_one_motivation = self.driver.find_element(*MainPageLocators.MOTIVATION)
        pick_one_motivation.click()

    def click_third_dropdown(self):
        click_amount = self.driver.find_element(*MainPageLocators.AMOUNT_DROPDOWN)
        click_amount.click()

    def pick_amount(self):
        pick_amount_class = self.driver.find_element(*MainPageLocators.AMOUNT)
        pick_amount_class.click()

    def click_find(self):
        submit_my_plan = self.driver.find_element(*MainPageLocators.SUBMIT_FIND_MY_PLAN)
        submit_my_plan.click()

class PricingPage(BasePage):

    def click_buy_plan(self):
        click_buy_plan = self.driver.find_element(*PricingPageLocators.BUY_STUDIO_PLAN)
        click_buy_plan.click()

class LoginPage(BasePage):

    search_text_elements = SearchTextElement()

    def input_valid_username(self):
        input_username = self.driver.find_element(*SecondPageLocators.INPUT_USERNAME_FIELD)
        input_username.send_keys("ruslana.wilson+1@gmail.com")

    def input_valid_password(self):
        input_username = self.driver.find_element(*SecondPageLocators.INPUT_PASSWORD_FIELD)
        input_username.send_keys("qweqwe123")

    def click_to_login(self):
        login_button = self.driver.find_element(*SecondPageLocators.LOGIN_BUTTON_ACTION)
        login_button.click()
        return "HAVE AN ACCOUNT? LOGIN HERE" not in self.driver.page_source


