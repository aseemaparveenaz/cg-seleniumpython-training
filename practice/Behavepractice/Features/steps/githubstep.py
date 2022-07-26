from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium_practice.gitlocator import GitLocator
@given("The user is in login page to login github")
def login(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://github.com/login")

@when(" The user enters the username of the github page")
def username(context):
    context.driver.find_element(By.ID, GitLocator.username).send_keys("uname")

@when("The user enters the password")
def password(context):
    context.driver.find_element(By.NAME, GitLocator.password).send_keys("xxx")

@Then("The user clicks the signin button")
def siginbutton(context):
    context.driver.find_element(By.XPATH, GitLocator.button)
