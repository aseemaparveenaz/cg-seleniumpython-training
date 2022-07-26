from selenium import webdriver
from selenium.webdriver.support.ui import Select
from behave import given, when, then
import time

@given('the user is on the search page')
def search(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://blazedemo.com/')

@when('the user selects Paris as a departure city')
def select(context):
    ele =Select(context.driver.find_element_by_name('fromPort'))
    ele.select_by_visible_text('Paris')
    time.sleep(2)

@when('the user selects London as a destination city')
def selectdest(context):
    elem = Select(context.driver.find_element_by_name('toPort'))
    elem.select_by_visible_text("London")
    time.sleep(2)

@when('clicks on the Find Flights button')
def submit(context):
    context.driver.find_element_by_xpath("//input[@type='submit']").click()
    time.sleep(5)

@then('flights are presented on the search result page')
def end(context):
    print('flights are presented on the search result page')