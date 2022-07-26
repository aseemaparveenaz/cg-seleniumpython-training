from behave import *
@given('we have behave installed')
def imp1_bk(context):
    print('Behave installed')
@when('we implement a test')
def imp2_bk(context):
    print('Implemented test')
@then('behave will test it for us')
def imp3_bk(context):
    print('Executed successfully')










#from behave import *
#@given('we have behave installed')
#def step_impl1(context):
 #   pass

#@when('we implement a test')
#def step_impl2(context):
 #   assert True is not False

#@then('behave will test it for us')
#def step_impl3(context):
 #   assert context.failed is False