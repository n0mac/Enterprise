from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_BUTTON = (By.XPATH, "html/body/div[1]/div[2]/div/a[2]")
    FIND_MY_PLAN_JS = (By.XPATH, "html/body/div[1]/div[2]/div/a[1]")
    GOAL_DROPDOWN = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[1]/a")
    GOAL = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[1]/ul/li[4]")
    MOTIVATION_DROPDOWN = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[2]/a")
    MOTIVATION = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[2]/ul/li[3]")
    AMOUNT_DROPDOWN = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[3]/a")
    AMOUNT = (By.XPATH, ".//*[@id='nl-form']/fieldset/div[3]/ul/li[2]")
    SUBMIT_FIND_MY_PLAN = (By.XPATH, ".//*[@id='nl-form']/fieldset/input")

class SecondPageLocators(object):
    LOGIN_BUTTON_ACTION = (By.NAME, "commit")
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

class AditionalInfoLocators(object):
    FIRST_NAME = (By.XPATH, ".//*[@id='user_first_name']")
    LAST_NAME = (By.XPATH, ".//*[@id='user_last_name']")
    BIRTHDATE = (By.XPATH, ".//*[@id='user_profile_attributes_birth_date']")
    ADDRESS = (By.XPATH, ".//*[@id='user_address_attributes_address']")
    CITY = (By.XPATH, ".//*[@id='user_address_attributes_city']")
    STATE = (By.XPATH, ".//*[@id='user_address_attributes_state']")
    COUNTRY = (By.XPATH, ".//*[@id='user_address_attributes_country']")
    POSTAL_CODE = (By.XPATH, ".//*[@id='user_address_attributes_zip_code']")
    MOBILE_PHONE = (By.XPATH, ".//*[@id='user_address_attributes_phone']")
    LOCATION = (By.XPATH, ".//*[@id='user_preferred_location']")
    GO_TO_BILLING = (By.NAME, "commit")

class BillingPageLocators(object):
    SAME_AS_REGISTRATION = (By.XPATH, ".//*[@id='new_billing_info']/fieldset[1]/ul/li[1]/label")
    BILLING_FNAME = (By.XPATH, ".//*[@id='billing_info_first_name']")
    BILLING_LNAME = (By.XPATH, ".//*[@id='billing_info_last_name']")
    BILLING_ADDRESS = (By.XPATH, ".//*[@id='billing_info_address']")
    BILLING_CITY = (By.XPATH, ".//*[@id='billing_info_city']")
    BILLING_STATE = (By.XPATH, ".//*[@id='billing_info_state']")
    BILLING_ZIP_CODE = (By.XPATH, ".//*[@id='billing_info_zip_code']")
    NAME_ON_CARD = (By.XPATH, ".//*[@id='billing_info_billing_name']")
    CARD_NUMBER = (By.XPATH, ".//*[@id='billing_info_card_number']")
    EXPIRY_MONTH = (By.XPATH, ".//*[@id='billing_info_exp_month']")
    EXPIRY_YEAR = (By.XPATH, ".//*[@id='billing_info_exp_year']")
    TERMS = (By.XPATH, ".//*[@id='new_billing_info']/fieldset[2]/div/label")
    PURCHASE = (By.CLASS_NAME, "agreements")
    HOME_BUTTON = (By.XPATH, "html/body/div[1]/div[1]/a/img")
    LOGOUT_BUTTON = (By.XPATH, "html/body/div[1]/div[2]/div/a[2]")

class DashboardPageLocators(object):
    CHANGE_WORKOUT_BUTTON = (By.XPATH, "html/body/div[1]/div[4]/section[2]/div[1]/div[3]/a[2]")
    CHANGE_WORKOUT_BUTTON_IF_RECOVERY = (By.XPATH, "html/body/div[1]/div[4]/section[2]/div[1]/div[3]/a")
    ODW_CONTINUE_BUTTON = (By.XPATH, "html/body/div[1]/div[4]/section/div/div[2]/a")
    LIVE_CONTINUE_BUTTON = (By.XPATH, "html/body/div[1]/div[4]/section/div/div[1]/a")
    RECOVERY_CONTINUE_BUTTON = (By.XPATH, "html/body/div[1]/div[4]/section/div/div[3]/a")
    SKIP_THIS_STEP_BUTTON = (By.XPATH, "html/body/div[1]/div[4]/section/a")

class AssertionIds(object):
    HOMEPAGE_TITLE = (By.XPATH, "html/body/div[1]/div[3]/div[1]/div[2]")
    PRICING_PAGE_TITLE = (By.XPATH, "html/body/div[1]/div[3]/div[1]/div[2]/span")
    NEW_REGISTRATION_TITLE = "existing Barretastic members"
    ALREADY_HAVE_PROGRAM_TITLE = "* You have already created an active program with this email address. Please login to view your program."
    PASSWORDS_NOT_MATCH = "* doesn't match Password"
    PASSWORDS_SHORT = "* is too short (minimum is 8 characters)"
    INCLUDE_NUMBER_LETTER = "* must include at least one letter and one number."
    ADDITIONAL_INFO_MATCH = "CREATE YOUR STUDIO ACCOUNT"
    ALREADY_CREATED_MINDBODY_ACC = "An account has already been created in MINDBODY with that email address. Please register as an existing user."
    CHOOSE_A_NEW_WORKOUT_TITLE = "CHOOSE A NEW WORKOUT"
    ON_DEMAND_WORKOUT_TITLE_ON_DASHBOARD = "On Demand Workout"
    RECOVERY_TITLE_ON_DASHBOARD = "Recovery day"
    LIVE_CLASS_TITLE_ON_DASHBOARD = "Class at Barretastic"







