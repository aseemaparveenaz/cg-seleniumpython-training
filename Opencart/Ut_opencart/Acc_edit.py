import unittest
from selenium import webdriver
import time
import openpyxl
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Ut_opencart.Locattor import Locatorr
from Ut_opencart import readwritefn
class Edit_Acc_page(unittest.TestCase):
    @classmethod
    def setUpClass(class_name):
      class_name.driver = webdriver.Chrome()
      class_name.driver.maximize_window()

    def setUp(self):
        print("test case executing...")

    def test0_login_valid(self):
        xl_file = r"C:\Users\ASEEAZ\Desktop\selenuim-python\opencart_project\opencartxlsheet.xlsx"
        workbook = openpyxl.load_workbook(xl_file)
        sheet = workbook.active
        rowcount = sheet.max_row
        print("Number of rows in excel: ", rowcount - 1)
        for curr_row in range(2, rowcount + 1):
            self.driver.get("https://www.opencart.com/index.php?route=account/login")
            xl_username = readwritefn.readData(sheet, curr_row, 1)
            xl_password = readwritefn.readData(sheet, curr_row, 2)
            xl_pin      = readwritefn.readData(sheet,curr_row,3)
            print("Username: {0} - Password: {1}".format(xl_username, xl_password))
            username = self.driver.find_element_by_id(Locatorr.email)
            username.clear()
            username.send_keys(xl_username)
            password = self.driver.find_element_by_id(Locatorr.pswd)
            password.clear()
            password.send_keys(xl_password)
            self.driver.find_element_by_xpath(Locatorr.loginbtn).click()
            time.sleep(5)
            try:
                if self.driver.find_element_by_id(Locatorr.pin).is_displayed():
                    pinn=self.driver.find_element_by_id(Locatorr.pin)
                    pinn.clear()
                    pinn.send_keys(xl_pin)
                    self.driver.find_element_by_xpath(Locatorr.subbtn).submit()
                    time.sleep(6)
            except NoSuchElementException:
                readwritefn.writeData(sheet, curr_row, 4, "failed")
        if (self.driver.title == "OpenCart - Your Account"):
            readwritefn.writeData(sheet, curr_row, 4, "passed")
            print('Login successful')
        else:
            print("login failed")
        workbook.save(xl_file)

    def test1_enter_acc_page(self):
        a=self.driver.find_element_by_link_text(Locatorr.acc_page).click()
        print("user entered into account page")
        time.sleep(10)

    #enter_username
        User_name = self.driver.find_element_by_name(Locatorr.usr)
        User_name.clear()
        User_name.send_keys("Aseema_parveen")
        print("username entered successfully !")
    #enter_fname
        Firstname =self.driver.find_element_by_name(Locatorr.fname)
        Firstname.clear()
        Firstname.send_keys("aseema")
        print("first name entered successfully !")

        # enter last name
        Lastname = self.driver.find_element_by_name(Locatorr.lname)
        Lastname.clear()
        Lastname.send_keys("AZ")
        print("last name entered successfully !")

        # enter company name
        Company = self.driver.find_element_by_name(Locatorr.comp)
        Company.clear()
        Company.send_keys("capgemini")
        print("company name entered successfully !")

        # enter taid
        TaxId = self.driver.find_element_by_name(Locatorr.taxid)
        TaxId.clear()
        TaxId.send_keys("nil")
        print("TaxId entered successfully !")

        # enter email
        E_mail = self.driver.find_element_by_name(Locatorr.email_)
        E_mail.clear()
        E_mail.send_keys('aseemaparveenaz@gmail.com')
        print("email entered successfully !")

        # select country name from dropdown box
        CountryName = Select(self.driver.find_element(By.ID,Locatorr.country))
        CountryName.select_by_value("99")
        print("country name selected successfully !")

        # select radio button
        string = "no"
        if (string == "no"):
            noti0 = self.driver.find_element_by_css_selector(Locatorr.noti_no)
            noti0.click()
            print("notification selected as no")
        else:
            noti1 = self.driver.find_element_by_css_selector(Locatorr.noti_yes)
            noti1.click()
            print("notification selected as yes")

        # click the button
        #wait=WebDriverWait(self.driver,10)
        make_changes = "yes"
        if (make_changes == "yes"):
            self.driver.find_element(By.XPATH,Locatorr.submit_but_acc).click()
            print("Account has been edited successfully")
        else:
            self.driver.find_element(By.XPATH,Locatorr.cancel_but_acc).click()
            print("Account has been not edited")

        #comback to previous page
        dashboard= self.driver.find_element_by_link_text(Locatorr.Dashboard)
        dashboard.click()

    def test2_change_password(self):
          #enter change password page by clicking it
          self.driver.find_element_by_link_text(Locatorr.change_pwd_page).click()

          #password generation
          oldpwd="xxx"
          strpwd=oldpwd[0:5]
          intpwd=int(oldpwd[5:])
          intpwd=intpwd+1
          intpwdstr=str(intpwd)
          newpass=strpwd+intpwdstr

          #enter current password
          Curr_Pwd=self.driver.find_element(By.NAME,Locatorr.curr_pwd)
          Curr_Pwd.send_keys(oldpwd)
          time.sleep(3)
          print("current password entered successfully")

          #enter neew password
          NewPassWord=self.driver.find_element(By.NAME,Locatorr.newpassword)
          NewPassWord.send_keys(newpass)
          time.sleep(4)
          print("newpassword entered successfully")

          #enter in the cnfirm password field
          ConfirmPassWord=self.driver.find_element(By.NAME,Locatorr.confirmpassword)
          ConfirmPassWord.send_keys(newpass)
          time.sleep(4)
          print("password is confirmed !")

          #click submit or cancel button
          makechanges="no"
          if(makechanges=="yes"):
              Cont_Button=self.driver.find_element_by_xpath(Locatorr.cont_button)
              Cont_Button.click()
              print("password Changed successfully!")
              time.sleep(10)
          else:
              Cancel_Button=self.driver.find_element_by_xpath(Locatorr.cancel_button)
              Cancel_Button.click()
              print("password not Changed !")
              time.sleep(10)

          #get back to previous page by clicking dash board
          self.driver.find_element_by_link_text("Dashboard")
    def test3_showcase_details(self):
        #enter into showcase page by clicking it
        Showcase_Page=self.driver.find_element_by_link_text(Locatorr.showcase_page).click()
        print("user entered the showcase page")

        #click add project button
        Add_Pro_Button=self.driver.find_element_by_xpath(Locatorr.add_pro_button)
        Add_Pro_Button.click()
        print("add project button is clicked")

        #enter shocwcase name
        Showcase_Name=self.driver.find_element_by_id(Locatorr.showcase_name).send_keys("CAR")
        print("show case name entered successfully")

        #enter showcase type from drop down
        ShowcaseType=Select(self.driver.find_element(By.ID,Locatorr.showcasetype))
        ShowcaseType.select_by_visible_text('Tech & Gadgets')
        print("show case type is selected successfully")
        time.sleep(2)

        #enter the launch date
        Launch_Date=self.driver.find_element(By.NAME,Locatorr.launch_date).send_keys("2021-10-08")
        print("launch date entered successfully")

        #enter weblink
        WebLink=(self.driver.find_element(By.ID,Locatorr.weblink))
        WebLink.clear()
        WebLink.send_keys("https://in.pinterest.com/")
        print("weblink entered successfully")


        print("image uploaded manually")
        #driver.find_element_by_xpath("//*[@id='account-showcase']/div/div/div[1]/form/fieldset[2]/div/div[1]/div/div").send_keys("C:/Users/ASEEAZ/Desktop/selenuim-python/car.jpg")
        time.sleep(20)

        #click button submit or cancel
        change="no"
        if(change=="yes"):
            submit_button=self.driver.find_element_by_xpath(Locatorr.submit_button).click()
            print("changes done !")
        else:
            CANCEL_button=self.driver.find_element_by_xpath(Locatorr.canc_show).click()
            print("changes not done")

        #comback to previous page
        time.sleep(5)
        self.driver.find_element_by_link_text(Locatorr.Dashboard).click()

    def test4_payment_module(self):
        #switvh to payment page by clicking it
        Pay_Page=self.driver.find_element_by_link_text(Locatorr.pay_page).click()
        print("user entered the payment page")

        #click add card button
        AddCard=self.driver.find_element_by_xpath(Locatorr.addcard).click()
        time.sleep(10)
        print("add card button is clicked")
        #click dropdown
        DropDowncre=self.driver.find_element_by_xpath(Locatorr.dropdowncre).click()
        print("credit card mode is selected !")

        time.sleep(25)
        print("credential entered manually")

        #enter the storebutton
        StoreButton=self.driver.find_element_by_id(Locatorr.storebutton).click()
        time.sleep(10)
        print("button is clicked")

    def tearDown(self):
        print("testcase executed")

    @classmethod
    def tearDownClass(class_name):
        class_name.driver.quit()
        print("All test execution completed...")
