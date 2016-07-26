from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "html/body/div[2]/div[2]/div/a[2]")
    FIND_MY_PLAN_JS = (By.XPATH, "html/body/div[1]/div[2]/div/a[1]")
    GOAL_DROPDOWN = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[1]/a")
    GOAL = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[1]/ul/li[4]")
    MOTIVATION_DROPDOWN = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[2]/a")
    MOTIVATION = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[2]/ul/li[3]")
    AMOUNT_DROPDOWN = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[3]/a")
    AMOUNT = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[3]/ul/li[2]")
    SUBMIT_FIND_MY_PLAN = (By.XPATH, ".//*[@id='nl-form']/fieldset/input")

class SecondPageLocators(object):
    LOGIN_BUTTON_ACTION = (By.XPATH, "html/body/div[2]/div[2]/div/div/form/fieldset/ul/input")
    INPUT_USERNAME_FIELD = (By.XPATH, ".//*[@id='user_email']")
    INPUT_PASSWORD_FIELD = (By.XPATH, ".//*[@id='user_password']")
    #pass

class PricingPageLocators(object):
    BUY_STUDIO_PLAN = (By.XPATH, ".//*[@id='select_workout_plan']/li/div/a")

class RegisterNewEmailLocators(object):
    NEW_MEMBER_TAB = (By.XPATH, ".//*[@id='new_member']/a")
    EMAIL_FIELD_NEW = (By.XPATH, ".//*[@id='new_user_email']")
    PASSWORD_FIELD_NEW = (By.XPATH, ".//*[@id='new_user_password']")
    CONFIRM_PASSWORD_FIELD_NEW = (By.XPATH, ".//*[@id='new_user_password_confirm']")
    NEXT_BUTTON = (By.XPATH, ".//*[@id='new_user']/fieldset/input")

class AssertionIds(object):
    HOMEPAGE_TITLE = (By.XPATH, "html/body/div[1]/div[3]/div[1]/div[2]")
    PRICING_PAGE_TITLE = (By.XPATH, "html/body/div[1]/div[3]/div[1]/div[2]/span")
    NEW_REGISTRATION_TITLE = (By.XPATH, "kaka")



