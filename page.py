from selenium.common.exceptions import NoSuchElementException
from element import BasePageElement
from locators import *
from selenium.webdriver.support.ui import Select


class SearchTextElement(BasePageElement):

    locator = "Login"

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.exeption = NoSuchElementException


class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_home_title_matches(self):
        return "Barretastic360" in self.driver.title

    def click_login_button(self):
        login = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        login.click()

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

class AssertsTitles(BasePage):

    def already_have_program(self):
        return AssertionIds.ALREADY_HAVE_PROGRAM_TITLE

    def passwords_not_match(self):
        return AssertionIds.PASSWORDS_NOT_MATCH

    def password_is_short(self):
        return AssertionIds.PASSWORDS_SHORT

    def email_registration_page(self):
        return AssertionIds.NEW_REGISTRATION_TITLE

    def must_include_letter_number(self):
        return AssertionIds.INCLUDE_NUMBER_LETTER

    def additional_info_page(self):
        return AssertionIds.ADDITIONAL_INFO_MATCH

    def check_mindbody_user_error(self):
        return AssertionIds.ALREADY_CREATED_MINDBODY_ACC

    def choose_a_new_workout_page(self):
        return AssertionIds.CHOOSE_A_NEW_WORKOUT_TITLE

    def odw_title_is_appeared(self):
        return AssertionIds.ON_DEMAND_WORKOUT_TITLE_ON_DASHBOARD

    def recovery_title_is_appeared(self):
        return AssertionIds.RECOVERY_TITLE_ON_DASHBOARD

    def live_class_title_is_appeared(self):
        return AssertionIds.LIVE_CLASS_TITLE_ON_DASHBOARD

class PricingPage(BasePage):

    def click_buy_plan(self):
        click_buy_plan = self.driver.find_element(*PricingPageLocators.BUY_STUDIO_PLAN)
        click_buy_plan.click()

    def is_pricing_title_matches(self):
        return "Barretastic360 | Learn More" in self.driver.title

class EmailRegistrationPage(BasePage):

    def click_new_member(self):
        click_tab_new = self.driver.find_element(*RegisterNewEmailLocators.NEW_MEMBER_TAB)
        click_tab_new.click()

    def input_email_new(self):
        input_new_email = self.driver.find_element(*RegisterNewEmailLocators.EMAIL_FIELD_NEW)
        input_new_email.send_keys("michael.boatman+322@gmail.com")

    def input_registered_username(self):
        input_username = self.driver.find_element(*RegisterNewEmailLocators.EMAIL_FIELD_NEW)
        input_username.send_keys("ruslana.wilson+1@gmail.com")

    def click_password_field(self):
        input_new_password = self.driver.find_element(*RegisterNewEmailLocators.PASSWORD_FIELD_NEW)
        input_new_password.send_keys("qweqwe123")

    def click_confirm_password_field(self):
        click_confirm_password_field = self.driver.find_element(*RegisterNewEmailLocators.CONFIRM_PASSWORD_FIELD_NEW)
        click_confirm_password_field.send_keys("qweqwe123")

    def click_next_button(self):
        next_button_go = self.driver.find_element(*RegisterNewEmailLocators.NEXT_BUTTON)
        next_button_go.click()

    def remove_invalid_email(self):
        remove_email = self.driver.find_element(*RegisterNewEmailLocators.EMAIL_FIELD_NEW)
        remove_email.clear()

    def input_valid_email(self):
        valid_email = self.driver.find_element(*RegisterNewEmailLocators.EMAIL_FIELD_NEW)
        valid_email.send_keys("michael.boatman+379@gmail.com")

    def input_not_match_password_confirm(self):
        input_not_matching_password = self.driver.find_element(*RegisterNewEmailLocators.CONFIRM_PASSWORD_FIELD_NEW)
        input_not_matching_password.send_keys("qwe")

    def short_password_input(self):
        input_not_matching_password = self.driver.find_element(*RegisterNewEmailLocators.PASSWORD_FIELD_NEW)
        input_not_matching_password.send_keys("qwe")


class LoginPage(BasePage):

    search_text_elements = SearchTextElement()

    def input_valid_username(self):
        input_username = self.driver.find_element(*SecondPageLocators.INPUT_USERNAME_FIELD)
        input_username.send_keys("ruslana.wilson+2@gmail.com")

    def input_valid_password(self):
        input_username = self.driver.find_element(*SecondPageLocators.INPUT_PASSWORD_FIELD)
        input_username.send_keys("qweqwe123")

    def click_to_login(self):
        login_button = self.driver.find_element(*SecondPageLocators.LOGIN_BUTTON_ACTION)
        login_button.click()

class AdditionalInfoPage(BasePage):

    def input_first_name(self):
        input_first_name = self.driver.find_element(*AditionalInfoLocators.FIRST_NAME)
        input_first_name.send_keys("Iaroslav")

    def input_last_name(self):
        input_last_name = self.driver.find_element(*AditionalInfoLocators.LAST_NAME)
        input_last_name.send_keys("Test")

    def input_birthdate(self):
        input_birthdate = self.driver.find_element(*AditionalInfoLocators.BIRTHDATE)
        input_birthdate.clear()
        input_birthdate.send_keys("10032000")

    def input_address(self):
        input_address = self.driver.find_element(*AditionalInfoLocators.ADDRESS)
        input_address.send_keys("Hoholya st. 100, apt. 4")

    def input_city(self):
        input_city = self.driver.find_element(*AditionalInfoLocators.CITY)
        input_city.send_keys("New York")

    def select_state(self):
        select_state = Select(self.driver.find_element(*AditionalInfoLocators.STATE))
        select_state.select_by_value("NY")

    def select_country(self):
        select_country = Select(self.driver.find_element(*AditionalInfoLocators.COUNTRY))
        select_country.select_by_value("US")

    def input_postal_code(self):
        input_postal_code = self.driver.find_element(*AditionalInfoLocators.POSTAL_CODE)
        input_postal_code.send_keys("1800JK")

    def input_mobile_phone(self):
        input_mobile = self.driver.find_element(*AditionalInfoLocators.MOBILE_PHONE)
        input_mobile.clear()
        input_mobile.send_keys("1231231234")

    def select_location(self):
        select_location = Select(self.driver.find_element(*AditionalInfoLocators.LOCATION))
        select_location.select_by_value("Barretastic")

    def go_to_billing_page(self):
        click_next = self.driver.find_element(*AditionalInfoLocators.GO_TO_BILLING)
        click_next.click()

class BillingPage(BasePage):

    def click_same_as_registration(self):
        click_checkbox = self.driver.find_element(*BillingPageLocators.SAME_AS_REGISTRATION)
        click_checkbox.click()

    def enter_firstname(self):
        enter_fname = self.driver.find_element(*BillingPageLocators.BILLING_FNAME)
        enter_fname.send_keys("iPhone")

    def enter_lastname(self):
        enter_lname = self.driver.find_element(*BillingPageLocators.BILLING_LNAME)
        enter_lname.send_keys("Profi")

    def enter_address(self):
        enter_address = self.driver.find_element(*BillingPageLocators.BILLING_ADDRESS)
        enter_address.send_keys("Hoholya 137, apt 24")

    def enter_city(self):
        enter_city = self.driver.find_element(*BillingPageLocators.BILLING_CITY)
        enter_city.send_keys("New Cherkasy")

    def select_billing_state(self):
        enter_state = Select(self.driver.find_element(*BillingPageLocators.BILLING_STATE))
        enter_state.select_by_value("CA")

    def enter_zip(self):
        enter_zip = self.driver.find_element(*BillingPageLocators.BILLING_ZIP_CODE)
        enter_zip.send_keys("18FY00")

    def enter_card_name(self):
        enter_card_name = self.driver.find_element(*BillingPageLocators.NAME_ON_CARD)
        enter_card_name.send_keys("Apostol the Great")

    def enter_card_number(self):
        enter_number = self.driver.find_element(*BillingPageLocators.CARD_NUMBER)
        enter_number.send_keys("4242424242424242")

    def enter_exp_month(self):
        enter_month = self.driver.find_element(*BillingPageLocators.EXPIRY_MONTH)
        enter_month.send_keys("10")

    def enter_exp_year(self):
        enter_year = self.driver.find_element(*BillingPageLocators.EXPIRY_YEAR)
        enter_year.send_keys("2020")

    def click_terms_checkbox(self):
        click_checkbox = self.driver.find_element(*BillingPageLocators.TERMS)
        click_checkbox.click()

    def click_purchase(self):
        purchase = self.driver.find_element(*BillingPageLocators.PURCHASE)
        purchase.click()

    def click_home_logo(self):
        logo = self.driver.find_element(*BillingPageLocators.HOME_BUTTON)
        logo.click()

    def click_logout(self):
        logout = self.driver.find_element(*BillingPageLocators.LOGOUT_BUTTON)
        logout.click()

class DashboardPage(BasePage):

    def is_dashboard_title_matches(self):
        return "Barretastic360 | Dashboard" in self.driver.title

    def click_change_workout_if_recovery(self):
        chage_workout = self.driver.find_element(*DashboardPageLocators.CHANGE_WORKOUT_BUTTON_IF_RECOVERY)
        chage_workout.click()

    def click_odw_continue(self):
        odw_continue = self.driver.find_element(*DashboardPageLocators.ODW_CONTINUE_BUTTON)
        odw_continue.click()

    def click_recovery_continue(self):
        recovery_continue = self.driver.find_element(*DashboardPageLocators.RECOVERY_CONTINUE_BUTTON)
        recovery_continue.click()

    def click_live_class_continue(self):
        live_class_continue = self.driver.find_element(*DashboardPageLocators.LIVE_CONTINUE_BUTTON)
        live_class_continue.click()

    def click_change_workout(self):
        elem = self.driver.find_element(*DashboardPageLocators.CHANGE_WORKOUT_BUTTON_IF_RECOVERY)
        try:
            elem2 = self.driver.find_element(*DashboardPageLocators.CHANGE_WORKOUT_BUTTON)
            elem2.click()
        except self.exeption:
            elem.click()

    def click_skip_thi_step(self):
        skip_this_step = self.driver.find_element(*DashboardPageLocators.SKIP_THIS_STEP_BUTTON)
        skip_this_step.click()













