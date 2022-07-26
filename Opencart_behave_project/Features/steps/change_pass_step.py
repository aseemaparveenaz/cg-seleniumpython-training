from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from behave import given, when, then
from Features.steps.Locator import Locatorr
import time
@given("The user is in the account page for entering into change password page")
def setup_function(context):
    driver = webdriver.Chrome()
    driver.maximize_window()
    context.driver.get("https://www.opencart.com/index.php?route=common/home")
    context.driver.find_element_by_link_text(Locatorr.login).click()
    context.driver.find_element_by_id(Locatorr.email).send_keys('xxxx')
    context.driver.find_element_by_id(Locatorr.pswd).send_keys('xxx')
    context.driver.find_element_by_xpath(Locatorr.loginbtn).submit()
    time.sleep(3)
     #enter pin in new window
    context.driver.find_element_by_id(Locatorr.pin).send_keys('xxx')
    context.driver.find_element_by_xpath(Locatorr.subbtn).submit()
    time.sleep(6)
    print('Login successful')

@when("The user enters the change password link to enter into change password page")
def enters_changepassword_page(context):
    context.driver.find_element_by_link_text(Locatorr.change_pwd_page).click()


@when("The user enters the old password in the old password field")
def enter_old_password(context):
    # password generation
    oldpwd = "xxxx"
    # enter current password
    Curr_Pwd = context.driver.find_element(By.NAME, Locatorr.curr_pwd)
    Curr_Pwd.send_keys(oldpwd)

@when("The user enters the new password in the new password field")
def enter_new_password(context):
    # password generation
    oldpwd = "xxxxx"
    strpwd = oldpwd[0:5]
    intpwd = int(oldpwd[5:])
    intpwd = intpwd + 1
    intpwdstr = str(intpwd)
    context.newpass = strpwd + intpwdstr
    # enter new password
    NewPassWord = context.driver.find_element(By.NAME, Locatorr.newpassword)
    NewPassWord.send_keys(context.newpass)

@when("And The user enters the new password again in the confirm password field")
def enter_confirm_password(context):
    # enter in the cnfirm password field
    ConfirmPassWord = context.driver.find_element(By.NAME, Locatorr.confirmpassword)
    ConfirmPassWord.send_keys(context.newpass)

@when("The user clicks the submit or cancel button to change the password or to discard the changes")
def click_sub_or_cancel(context):
    # click submit or cancel button
    makechanges = "no"
    if (makechanges == "yes"):
        Cont_Button = context.driver.find_element_by_xpath(Locatorr.cont_button)
        Cont_Button.click()
        print("password Changed successfully!")
    else:
        Cancel_Button = context.driver.find_element_by_xpath(Locatorr.cancel_button)
        Cancel_Button.click()
        print("password not Changed !")
        time.sleep(2)

@then("The user come back from change password page to account page by clickig dashboard")
def dashboard2(context):
    # get back to previous page by clicking dash board
    self.driver.find_element_by_link_text("Dashboard")

