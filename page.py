from element import BasePageElement
from locators import MainPageLocators, SecondPageLocators

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


