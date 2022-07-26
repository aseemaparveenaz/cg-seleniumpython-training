from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from behave import given, when, then
from Locator import Locatorr
import time

@given("The user is in the account page after entering credentials")
def setup_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.opencart.com/index.php?route=common/home")
    context.driver.find_element_by_link_text(Locatorr.login).click()
    context.driver.find_element_by_id(Locatorr.email).send_keys('uname')
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

@then("The user enters the {user_n} in username field after entering into edit account page")
def enter_username(context, user_n):
    User_name = context.driver.find_element_by_name(Locatorr.usr)
    User_name.clear()
    User_name.send_keys(user_n)
    print("username entered")

@then("The user enters the {first_n} in the first name field")
def enter_fname(context,first_n):
    Firstname = context.driver.find_element_by_name(Locatorr.fname)
    Firstname.clear()
    Firstname.send_keys(first_n)

@then("The user enters the {last_n} in the last name field")
def enter_lname(context,last_n):
    Lastname = context.driver.find_element_by_name(Locatorr.lname)
    Lastname.clear()
    Lastname.send_keys(last_n)

@then("The user enters the {company_n} in the company name field")
def enter_company_name(context,company_n):
    Company = context.driver.find_element_by_name(Locatorr.comp)
    Company.clear()
    Company.send_keys(company_n)

@then("The user enters the {tax_Id} in the taxId field")
def enter_taxid(context,tax_Id):
    TaxId = context.driver.find_element_by_name(Locatorr.taxid)
    TaxId.clear()
    TaxId.send_keys(tax_Id)

@then("The user enters the {e_mail} in the email field")
def enter_email(context,e_mail):
    E_mail = context.driver.find_element_by_name(Locatorr.email_)
    E_mail.clear()
    E_mail.send_keys(e_mail)

@then("The user selects the {country_n} from the drop down list")
def select_country(context,country_n):
    CountryName = Select(context.driver.find_element(By.ID, Locatorr.country))
    CountryName.select_by_value(country_n)

@then("The user selects the radio button yes or no for notification preferences given in {radio_str}")
def select_noti(context,radio_str):
    #string="no"
    if (radio_str== "no"):
        noti0 = context.driver.find_element_by_css_selector(Locatorr.noti_no)
        noti0.click()
    else:
        noti1 = context.driver.find_element_by_css_selector(Locatorr.noti_yes)
        noti1.click()

@when("The user clicks on the submit or cancel button to save or discard the new information given as {click_btn}")
def click_sub_or_can_button(context,click_btn):
    #make_changes = "yes"
    if (click_btn == "yes"):
        context.driver.find_element(By.XPATH, Locatorr.submit_but_acc).click()
        print("account has been edited successfully")
    else:
        context.driver.find_element(By.XPATH, Locatorr.cancel_but_acc).click()
        print("account has been not edited")

@then("The user Clicks the Dashboard link to come back to account details page from edit account page")
def click_dash1(context):
    context.driver.find_element_by_link_text(Locatorr.Dashboard).click()
