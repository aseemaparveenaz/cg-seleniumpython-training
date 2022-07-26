from behave import *

@given('the ninja has a third level black-belt')
def fun1(context):
    print("The ninja has third level black-belt")

@when('attacked by samurai')
def fun2(context):
    print("Ninja attacked")

@then('the ninja should engage the opponent')
def fun3(context):
    print("Engaged the opponent")

@given('the ninja has a first level black-belt')
def fun4(context):
    print("First level black belt")

@when('attacked by Chuck Norris')
def fun5(context):
    print("chuck norris attacked")

@then('the ninja should run for his life')
def fun6(context):
    print('ninja ran')