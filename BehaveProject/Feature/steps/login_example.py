import time
from behave import given, when, then, step
from selenium import webdriver
@given('i go to my login form')
def go_to_login_form(context):
    context.driver=webdriver.Chrome()
    context.driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
@then('the title should be {text}')
def verify_title(context,text):
    title = context.driver.title
    try:
        assert "Rediff.com: News | Rediffmail | stock Quotes | shopping" == title
    except AssertionError as e:
        print(e)
@when('I enter my credentials')
def enter_credentials(context):
    context.driver.find_element_by_id('login1').send_keys('uname')
    context.driver.find_element_by_id('password').send_keys('xxx')
    time.sleep(20)
@when('I click login')
def click_login(context):
    context.driver.find_element_by_name('proceed').click()
