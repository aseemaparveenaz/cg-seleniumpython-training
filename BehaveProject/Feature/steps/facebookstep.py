behave from behave import *
from selenium import webdriver
import time

@given('user launch browser')
def launch(context):
    context.driver = webdriver.Chrome()

@when('user open rediff')
def open(context):
    context.driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

@when('user enter {name} and {password}')
def credentials(context, name, password):
    context.driver.find_element_by_id('login1').send_keys(name)
    context.driver.find_element_by_id('password').send_keys(password)
    time.sleep(5)

@when('user clicks on login')
def submit(context):
    context.driver.find_element_by_name('proceed').click()

@Then('user should be able to logged in')
def msg(context):
    print('User get logged in')