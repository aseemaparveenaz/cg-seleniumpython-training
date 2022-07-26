class Locatorr(object):
    # --name
    usr = "username"
    fname = "firstname"
    lname = "lastname"
    comp = "company"
    taxid = "tax_id"
    email_ = "email"  # --name
    country = 'input-country'  # id
    noti_no = "input[value='0']"  # --css selector
    noti_yes = "input[value='1']"  # ---css selector
    submit_but_acc = "//*[@id='account-edit']/div/div/div[1]/form/div/button"  # xpath
    cancel_but_acc = "//*[@id='account-edit']/div/div/div[1]/form/div/a"  # xpath
    Dashboard = "Dashboard"  # linktext
    acc_page = "Edit your account details"  # link text

    # -------change password
    change_pwd_page = "Reset your password"  # linktext
    curr_pwd = 'current'  # name
    newpassword = 'password'  # name
    confirmpassword = 'confirm'  # name
    cont_button = "//*[@id='account-password']/div/div/div[1]/form/div/button"  # xpath
    cancel_button = "//*[@id='account-password']/div/div/div[1]/form/div/a"  # xpath

    # -------payment
    pay_page = "Modify your payment methods"  # linktext
    addcard = "//*[@id='paymentDropdown']"  # xpath
    storebutton = "button-continue"  # xpath
    dropdowncre = "//*[@id='account-payment']/div/div/div[1]/fieldset/div[2]/span/ul/li[1]/a"

    # -----showcase details
    showcase_page = "Submit your store to OpenCart's showcase"  # linktext
    add_pro_button = "//*[@id='account-showcase']/div[2]/div/div[1]/div/a[2]"  # xpath
    showcase_name = "input-name"  # name
    showcasetype = "input-category"  # id
    launch_date = "date_launch"  # name
    weblink = "input-link"  # id
    submit_button = "//*[@id='account-showcase']/div/div/div[1]/form/div/button"  # xpth
    canc_show = "//*[@id='account-showcase']/div/div/div[1]/form/div/a"  # xpath

    login = "Login"
    email = "input-email"
    pswd = "input-password"
    loginbtn = "//div[@class='col-sm-6']/child::button[1]"
    pin = "input-pin"
    subbtn = '//div[@class="form-group"]/child::button'