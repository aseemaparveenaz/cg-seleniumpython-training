from behave import *
@given ('school details')
def impl_bk(context):
    print('school details entered')
@then('verify school name')
def impl1_bk(context):
    print('verify school name')