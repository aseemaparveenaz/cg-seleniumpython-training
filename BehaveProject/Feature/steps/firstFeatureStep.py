from behave import *
@given('Book details')
def impl_bk1(context):
    print('Book details entered')
@then('Verify book name')
def impl_bk2(context):
    print('Verify book name')