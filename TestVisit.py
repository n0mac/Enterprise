import unittest
from selenium import webdriver
import page
import time
import pymssql
from selenium.common.exceptions import NoSuchElementException

class Home(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://barretastic.m3v.us/")
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        #self.conn=pymssql.connect(host='dev05.m3v.us',user='booya',password='',database='postgres')

        #self.wait = WebDriverWait(self.driver, 1)

    '''def test_verify(self):
        conn = self.conn
        cursor = conn.cursor(as_dict=True)
        cursor.execute('select * from users where id = 2')
        records=cursor.fetchall()
        cursor.close()
        print records
        department_names=[]
        for record in records:
            department_name=record.get('Name')
            department_names.append(department_name)
            print department_name
        print "total records=%d" % len(department_names)
        self.assertTrue(department_names.index('PAPA') !=-1)'''



    def test_login_functionality(self):
        #components
        home_page = page.MainPage(self.driver)
        pricing_page = page.PricingPage(self.driver)
        email_registration_page = page.EmailRegistrationPage(self.driver)
        additional_information = page.AdditionalInfoPage(self.driver)
        billing_page = page.BillingPage(self.driver)
        login_page = page.LoginPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        asserts = page.AssertsTitles(self.driver)

        #check that homepage is opened
        assert home_page.is_home_title_matches(), "Title doesn't match"

        #check that find my plan button in the header is scrolling to the Mad Lib section
        '''home_page.click_find_my_plan_header_button()

        #check pickers in Mad Lib section, pick some values
        home_page.click_first_dropdown()
        home_page.pick_goal()
        time.sleep(0.3)
        home_page.click_second_dropdown()
        home_page.pick_motivation()
        time.sleep(0.4)
        home_page.click_third_dropdown()
        home_page.pick_amount()
        time.sleep(0.4)
        home_page.click_find()

        #check that pricing page is opened
        assert pricing_page.is_pricing_title_matches(), "Title doesn't match"

        #click on any package to buy it
        pricing_page.click_buy_plan()

        #check that email registration page is opened
        assert asserts.email_registration_page() in self.driver.page_source

        #check that already registered user can not be registered again
        email_registration_page.click_new_member()
        email_registration_page.input_email_new()
        email_registration_page.click_password_field()
        email_registration_page.click_confirm_password_field()
        email_registration_page.click_next_button()
        assert asserts.already_have_program() in self.driver.page_source

        #check that user can not be registered with passwords that don't match
        email_registration_page.remove_invalid_email()
        email_registration_page.input_valid_email()
        email_registration_page.click_password_field()
        email_registration_page.input_not_match_password_confirm()
        email_registration_page.click_next_button()
        assert asserts.passwords_not_match() in self.driver.page_source

        #check if too short passwords and if password must include at least one letter and one number
        email_registration_page.short_password_input()
        email_registration_page.input_not_match_password_confirm()
        email_registration_page.click_next_button()
        assert asserts.password_is_short() in self.driver.page_source
        assert asserts.must_include_letter_number() in self.driver.page_source

        #check already registered user with program
        email_registration_page.remove_invalid_email()
        email_registration_page.input_registered_username()
        email_registration_page.click_password_field()
        email_registration_page.click_confirm_password_field()
        email_registration_page.click_next_button()

        #check that error message is displayed on existing member tab
        assert asserts.check_mindbody_user_error() in self.driver.page_source

        #check valid credentials for email registration page
        email_registration_page.click_new_member()
        email_registration_page.input_valid_email()
        email_registration_page.click_password_field()
        email_registration_page.click_confirm_password_field()
        email_registration_page.click_next_button()

        #check if user is redirected to additional info page
        assert asserts.additional_info_page() in self.driver.page_source

        #check additional info with valid information entered
        additional_information.input_first_name()
        additional_information.input_last_name()
        additional_information.input_birthdate()
        additional_information.input_address()
        additional_information.input_city()
        additional_information.select_state()
        additional_information.select_country()
        additional_information.input_postal_code()
        additional_information.input_mobile_phone()
        additional_information.select_location()
        additional_information.go_to_billing_page()

        #check billing page with valid information entered
            #1.BILLING ADDRESS
        billing_page.click_same_as_registration()
        billing_page.click_same_as_registration()
        time.sleep(2)
        billing_page.enter_firstname()
        billing_page.enter_lastname()
        billing_page.enter_address()
        billing_page.enter_city()
        billing_page.select_billing_state()
        billing_page.enter_zip()
            #2.CREDIT CARD
        billing_page.enter_card_name()
        billing_page.enter_card_number()
        billing_page.enter_exp_month()
        billing_page.enter_exp_year()
            #billing_page.click_terms_checkbox()

        #check that user is redirected to homepage
        assert home_page.is_home_title_matches(), "Title doesn't match"
        billing_page.click_home_logo()

        #check that homepage is opened and user is logged out
        assert home_page.is_home_title_matches(), "Title doesn't match"
        billing_page.click_logout()

        #Confirm that after login dashboard page is opened'''


        #login with existing user
        home_page.click_login_button()
        login_page.input_valid_username()
        login_page.input_valid_password()
        login_page.click_to_login()

        #Confirm that after login dashboard page is opened
        assert dashboard_page.is_dashboard_title_matches(), "Title doesn't match"

        #click change workout for today from dashboard to open choose new workout page
        dashboard_page.click_change_workout()

        #Confirm that CHOOSE A NEW WORKOUT page is opened
        assert asserts.choose_a_new_workout_page() in self.driver.page_source

        #Change workout to on demand workout
        dashboard_page.click_odw_continue()

        #Confirm that workout was changed to on demand workout and dashboard page is opened
        assert dashboard_page.is_dashboard_title_matches(), "Title doesn't match"
        assert asserts.odw_title_is_appeared() in self.driver.page_source

        #click change workout for today again from dashboard to open choose new workout page
        dashboard_page.click_change_workout()

        #Confirm that CHOOSE A NEW WORKOUT page is opened
        assert asserts.choose_a_new_workout_page() in self.driver.page_source

        #Change workout to Recovery Day
        dashboard_page.click_recovery_continue()

        #Confirm that workout was changed to recovery and dashboard page is opened
        assert dashboard_page.is_dashboard_title_matches(), "Title doesn't match"
        assert asserts.recovery_title_is_appeared() in self.driver.page_source

        #click change workout for today again from dashboard to open choose new workout page
        dashboard_page.click_change_workout()

        #Confirm that CHOOSE A NEW WORKOUT page is opened
        assert asserts.choose_a_new_workout_page() in self.driver.page_source

        #Change workout to Live Class
        dashboard_page.click_live_class_continue()

        #Confirm that workout was changed to recovery and dashboard page is opened
        assert dashboard_page.is_dashboard_title_matches(), "Title doesn't match"
        assert asserts.live_class_title_is_appeared() in self.driver.page_source

        #click change workout for today again from dashboard to open choose new workout page
        dashboard_page.click_change_workout()

        #Confirm that CHOOSE A NEW WORKOUT page is opened
        assert asserts.choose_a_new_workout_page() in self.driver.page_source

        #Check skip this step functionality on CHOOSE A NEW WORKOUT page
        dashboard_page.click_skip_thi_step()

        #Confirm that workout was changed to recovery and dashboard page is opened
        assert dashboard_page.is_dashboard_title_matches(), "Title doesn't match"

        #Class booking through dashboard



    #def tearDown(self):
        #self.driver.close()

if __name__ == "__main__":
    unittest.main()
