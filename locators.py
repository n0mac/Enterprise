from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "html/body/div[2]/div[2]/div/a[2]")

class SecondPageLocators(object):
    LOGIN_BUTTON_ACTION = (By.XPATH, "html/body/div[2]/div[2]/div/div/form/fieldset/ul/input")
    #pass
