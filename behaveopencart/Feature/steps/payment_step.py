from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from behave import given, when, then
from Locator import Locatorr
import time

@given("The user is in Account page to enter into payment page")
def enter_acc_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.opencart.com/index.php?route=common/home")
    context.driver.find_element_by_link_text(Locatorr.login).click()
    context.driver.find_element_by_id(Locatorr.email).send_keys('uname')
    context.driver.find_element_by_id(Locatorr.pswd).send_keys('xxxx')
    context.driver.find_element_by_xpath(Locatorr.loginbtn).submit()
    time.sleep(3)
     #enter pin in new window
    context.driver.find_element_by_id(Locatorr.pin).send_keys('xxxx')
    context.driver.find_element_by_xpath(Locatorr.subbtn).submit()
    time.sleep(6)
    print('Login successful')

@when("The user click on the payment page link to move to payment page")
def go_to_payment(context):
    # switvh to payment page by clicking it
    Pay_Page = context.driver.find_element_by_link_text(Locatorr.pay_page).click()
    print("user entered the payment page")

@when("The user click on Add payment method button to store the card")
def click_addpayment(context):
    # click add card button
    AddCard = context.driver.find_element_by_xpath(Locatorr.addcard).click()
    time.sleep(5)

@when("The user select the credit card option from the dropdown")
def select_method(context):
    # click dropdown
    DropDowncre = context.driver.find_element_by_xpath(Locatorr.dropdowncre).click()
    time.sleep(20)
    print("credential entered manually")

@then("The user click on store card button to save the credit card")
def click_save(context):
    # enter the storebutton
    StoreButton = context.driver.find_element_by_id(Locatorr.storebutton).click()
    time.sleep(10)
    print("button is clicked")