from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from behave import given, when, then
from Features.steps.Locator import Locatorr
import time

@given("The user is in the account page for entering into showcase page")
def setup_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.opencart.com/index.php?route=common/home")
    context.driver.find_element_by_link_text(Locatorr.login).click()
    context.driver.find_element_by_id(Locatorr.email).send_keys('xxx')
    context.driver.find_element_by_id(Locatorr.pswd).send_keys('xxx')
    context.driver.find_element_by_xpath(Locatorr.loginbtn).submit()
    time.sleep(3)
     #enter pin in new window
    context.driver.find_element_by_id(Locatorr.pin).send_keys('xxx')
    context.driver.find_element_by_xpath(Locatorr.subbtn).submit()
    time.sleep(6)
    print('Login successful')

@when("The user enters the showcase page by clicking the showcase page link")
def enter_showcase_page(context):
    # enter into showcase page by clicking it
    Showcase_Page = context.driver.find_element_by_link_text(Locatorr.showcase_page).click()
    print("user entered the showcase page")

@when("The user clicks on the add project button to add projects in show case page")
def add_project(context):
    # click add project button
    Add_Pro_Button = context.driver.find_element_by_xpath(Locatorr.add_pro_button)
    Add_Pro_Button.click()
    print("add project button is clicked")

@then("The user enters the showcase name in the showcase name field")
def enter_showcase_name(context):
    # enter shocwcase name
    Showcase_Name = context.driver.find_element_by_id(Locatorr.showcase_name).send_keys("CAR")

@when("The user selects the showcase type from the dropdown list")
def select_showcase_type(context):
    # enter showcase type from drop down
    ShowcaseType = Select(context.driver.find_element(By.ID, Locatorr.showcasetype))
    ShowcaseType.select_by_visible_text('Tech & Gadgets')
    time.sleep(2)

@when("The user enters the launch date in the date field")
def enter_launch_date(context):
    # enter the launch date
    Launch_Date = context.driver.find_element(By.NAME, Locatorr.launch_date).send_keys("2021-10-08")

@when("The user enters the website in the website field")
def enter_website(context):
    # enter weblink
    WebLink = (context.driver.find_element(By.ID, Locatorr.weblink))
    WebLink.clear()
    WebLink.send_keys("https://in.pinterest.com/")

@when("The user clicks on the submit or cancel button save or discard the changes")
def click_save_or_discard(context):
    print("image uploaded manually")
    time.sleep(20)
    # click button submit or cancel
    change = "no"
    if (change == "yes"):
        submit_button = context.driver.find_element_by_xpath(Locatorr.submit_button).click()
    else:
        CANCEL_button = context.driver.find_element_by_xpath(Locatorr.canc_show).click()

@then("The user clicks on the dashboard to come out from showcase page to the account page")
def move_showcasepg_to_acc_page(context):
    # comback to previous page
    context.driver.find_element_by_link_text(Locatorr.Dashboard).click()

