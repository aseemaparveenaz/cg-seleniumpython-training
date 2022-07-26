from behave import *
@given('launch application')
def launch_application(context):
    print('launch application')

@then ('input credentials')
def input_credentials(context):
    print('input credentials')

@given('user is on credit card payment screen')
def credit_card_pay(context):
    print('user is on credit card payment screen')

@then('user should be able to complete credit card payment')
def credit_card_pay_comp(context):
    print('user should be able to complete credit card payment')

@given('user is on debit card payment screen')
def debit_card_pay(context):
    print('user is on debit card payment screen')

@then('user should be able to complete debit card payment')
def debit_card_pay_comp(context):
    print('user should be able to complete debit card payment')