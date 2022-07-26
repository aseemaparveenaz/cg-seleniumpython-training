from behave import *
from selenium import webdriver

@given('user is on home page')
def open_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.actitime.com/login.do")

@then('heading should be "Please identify yourself"')
def check_title(context):
    heading = context.driver.find_element_by_id('headerContainer')

    if heading.text == "Please identify yourself":
        print("Title matches")
    else:
        print("Title does not match")

@then('attribute of username should be printed')
def print_attribute(context):
    username = context.driver.find_element_by_id('username')
    type = username.get_attribute("type")
    print("Type attribute of Username: ", type)