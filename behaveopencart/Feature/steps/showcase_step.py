from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from behave import given, when, then
from Locator import Locatorr
import time

@given("The user is in the account page for entering into showcase page")
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
    context.driver.find_element_by_id(Locatorr.pin).send_keys('xxxx')
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

@then("The user enters the {showcase_n} in the showcase name field")
def enter_showcase_name(context,showcase_n):
    # enter shocwcase name
    Showcase_Name = context.driver.find_element_by_id(Locatorr.showcase_name).send_keys(showcase_n)

@then("The user selects the {showcase_typ} from the dropdown list")
def select_showcase_type(context,showcase_typ):
    # enter showcase type from drop down
    ShowcaseType = Select(context.driver.find_element(By.ID, Locatorr.showcasetype))
    ShowcaseType.select_by_visible_text(showcase_typ)
    time.sleep(2)

@when("The user enters the {launch_dt} in the date field")
def enter_launch_date(context,launch_dt):
    # enter the launch date
    Launch_Date = context.driver.find_element(By.NAME, Locatorr.launch_date).send_keys(launch_dt)

@when("The user enters the {wb_site} in the website field")
def enter_website(context,wb_site):
    # enter weblink
    WebLink = (context.driver.find_element(By.ID, Locatorr.weblink))
    WebLink.clear()
    WebLink.send_keys(wb_site)

@when("The user clicks on the submit or cancel button to save or discard the changes given as {this_button} string")
def click_save_or_discard(context,this_button):
    print("image uploaded manually")
    time.sleep(20)
    # click button submit or cancel
    #change = "no"
    if (this_button == "yes"):
        submit_button = context.driver.find_element_by_xpath(Locatorr.submit_button).click()
    else:
        CANCEL_button = context.driver.find_element_by_xpath(Locatorr.canc_show).click()

@then("The user clicks on the dashboard to come out from showcase page to the account page")
def move_showcasepg_to_acc_page(context):
    # comback to previous page
    context.driver.find_element_by_link_text(Locatorr.Dashboard).click()

