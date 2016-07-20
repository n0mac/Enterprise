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

    def click_login_button_loginpage(self):
        login_button = self.driver.find_element(*SecondPageLocators.LOGIN_BUTTON_ACTION)
        login_button.click()
        return "HAVE AN ACCOUNT? LOGIN HERE" not in self.driver.page_source
