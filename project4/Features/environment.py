def before_all(context):
    print("Before all executed")

def after_all(context):
    print("After all executed")

def before_feature(scenario, context):
    print("Before feature")

def after_feature(scenario, context):
    print("After feature")

def before_scenario(scenario, context):
    print("Before scenario")

def after_scenario(scenario, context):
    print("After scenario")

def before_step(scenario, context):
    print("Before step")

def after_step(scenario, context):
    print("After step")

def before_tag(scenario, context):
    print("Before tag")

def after_tag(scenario, context):
    print("After tag")