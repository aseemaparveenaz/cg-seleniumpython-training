from selenium import webdriver
from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from behave import given, when, then
from Features.steps.Locator import Locatorr
import time

@given("The user is in the account page after entering credentials")
def setup_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.opencart.com/index.php?route=common/home")
    context.driver.find_element_by_link_text(Locatorr.login).click()
    context.driver.find_element_by_id(Locatorr.email).send_keys('xxxx')
    context.driver.find_element_by_id(Locatorr.pswd).send_keys('xxxx')
    context.driver.find_element_by_xpath(Locatorr.loginbtn).submit()
    time.sleep(3)
     #enter pin in new window
    context.driver.find_element_by_id(Locatorr.pin).send_keys('xxx')
    context.driver.find_element_by_xpath(Locatorr.subbtn).submit()
    time.sleep(6)
    print('Login successful')

@when("The user click on the edit account link to enter into edit account page")
def edit_acc_click(context):
    a = context.driver.find_element_by_link_text(Locatorr.acc_page).click()
    print("user entered into account page")
    time.sleep(10)

@then("The user enters the username in username field after entering into edit account page")
def enter_username(context):
    User_name = context.driver.find_element_by_name(Locatorr.usr)
    User_name.clear()
    User_name.send_keys("Aseema_parveen")
    print("username entered")

@then("The user enters the firstname in the first name field")
def enter_fname(c.ontext):
    Firstname = context.driver.find_element_by_name(Locatorr.fname)
    Firstname.clear()
    Firstname.send_keys("aseema")

@then("The user enters the lastname in the last name field")
def enter_lname(context):
    Lastname = context.driver.find_element_by_name(Locatorr.lname)
    Lastname.clear()
    Lastname.send_keys("AZ")

@then("The user enters the company name in the company name field")
def enter_company_name(context):
    Company = context.driver.find_element_by_name(Locatorr.comp)
    Company.clear()
    Company.send_keys("capgemini")

@then("The user enters the taxId in the taxId field")
def enter_taxid(context):
    TaxId = context.driver.find_element_by_name(Locatorr.taxid)
    TaxId.clear()
    TaxId.send_keys("nil")

@then("The user enters the email in the email field")
def enter_email(context):
    E_mail = context.driver.find_element_by_name(Locatorr.email_)
    E_mail.clear()
    E_mail.send_keys('aseemaparveenaz@gmail.com')

@then("The user selects the country from the drop down list")
def select_country(context):
    CountryName = Select(context.driver.find_element(By.ID, Locatorr.country))
    CountryName.select_by_value("99")

@then("The user selects the radio button yes or no for notification preferences")
def select_noti(context):
    string = "no"
    if (string == "no"):
        noti0 = context.driver.find_element_by_css_selector(Locatorr.noti_no)
        noti0.click()
    else:
        noti1 = context.driver.find_element_by_css_selector(Locatorr.noti_yes)
        noti1.click()

@when("The user clicks on the submit or cancel button to save or discard the new information")
def click_sub_or_can_button(context):
    make_changes = "yes"
    if (make_changes == "yes"):
        context.driver.find_element(By.XPATH, Locatorr.submit_but_acc).click()
        print("account has been edited successfully")
    else:
        self.driver.find_element(By.XPATH, Locatorr.cancel_but_acc).click()
        print("account has been not edited")

@then("The user Clicks the Dashboard link to come back to account_details page from edit account page")
def click_dash1(context):
    context.driver.find_element_by_link_text(Locatorr.Dashboard).click()
