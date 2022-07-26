import unittest
from selenium import webdriver
import time
import openpyxl
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from roughaccdir.Locattor import Locatorr
class Edit_Acc_page(unittest.TestCase):
    @classmethod
    def setUpClass(class_name):
      class_name.driver = webdriver.Chrome()
      class_name.driver.maximize_window()

    def setUp(self):
        print("test case executing...")

    def test0_Login_valid(self):
        self.driver.get("https://www.opencart.com/index.php?route=common/home")
        self.driver.find_element_by_link_text(Locatorr.login).click()
        self.driver.find_element_by_id(Locatorr.email).send_keys('xxx')
        self.driver.find_element_by_id(Locatorr.pswd).send_keys('xxx')
        self.driver.find_element_by_xpath(Locatorr.loginbtn).submit()
        time.sleep(3)
        # enter pin in new window
        self.driver.find_element_by_id(Locatorr.pin).send_keys('xxx')
        self.driver.find_element_by_xpath(Locatorr.subbtn).submit()
        time.sleep(6)
        print('Login successful')

    def test1_enter_acc_page(self):
        a=self.driver.find_element_by_link_text(Locatorr.acc_page).click()
        print("user entered into account page")
        time.sleep(10)

    #enter_username
        User_name = self.driver.find_element_by_name(Locatorr.usr)
        User_name.clear()
        User_name.send_keys("Aseema_parveen")
        print("username entered")
    #enter_fname
        Firstname =self.driver.find_element_by_name(Locatorr.fname)
        Firstname.clear()
        Firstname.send_keys("aseema")

        # enter last name
        Lastname = self.driver.find_element_by_name(Locatorr.lname)
        Lastname.clear()
        Lastname.send_keys("AZ")

        # enter company name
        Company = self.driver.find_element_by_name(Locatorr.comp)
        Company.clear()
        Company.send_keys("capgemini")

        # enter taid
        TaxId = self.driver.find_element_by_name(Locatorr.taxid)
        TaxId.clear()
        TaxId.send_keys("nil")

        # enter email
        E_mail = self.driver.find_element_by_name(Locatorr.email_)
        E_mail.clear()
        E_mail.send_keys('aseemaparveenaz@gmail.com')

        # select country name from dropdown box
        CountryName = Select(self.driver.find_element(By.ID,Locatorr.country))
        CountryName.select_by_value("99")

        # select radio button
        string = "no"
        if (string == "no"):
            noti0 = self.driver.find_element_by_css_selector(Locatorr.noti_no)
            noti0.click()
        else:
            noti1 = self.driver.find_element_by_css_selector(Locatorr.noti_yes)
            noti1.click()

        # click the button
        #wait=WebDriverWait(self.driver,10)
        make_changes = "yes"
        if (make_changes == "yes"):
            self.driver.find_element(By.XPATH,Locatorr.submit_but_acc).click()
            print("account has been edited successfully")
        else:
            self.driver.find_element(By.XPATH,Locatorr.cancel_but_acc).click()
            print("account has been not edited")
        # driver.find_element_by_link_text("CANCEL").click()
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

          #enter neew password
          NewPassWord=self.driver.find_element(By.NAME,Locatorr.newpassword)
          NewPassWord.send_keys(newpass)

          #enter in the cnfirm password field
          ConfirmPassWord=self.driver.find_element(By.NAME,Locatorr.confirmpassword)
          ConfirmPassWord.send_keys(newpass)

          #click submit or cancel button
          makechanges="no"
          if(makechanges=="yes"):
              Cont_Button=self.driver.find_element_by_xpath(Locatorr.cont_button)
              Cont_Button.click()
              print("password Changed successfully!")
          else:
              Cancel_Button=self.driver.find_element_by_xpath(Locatorr.cancel_button)
              Cancel_Button.click()
              print("password not Changed !")

          time.sleep(2)
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

        #enter showcase type from drop down
        ShowcaseType=Select(self.driver.find_element(By.ID,Locatorr.showcasetype))
        ShowcaseType.select_by_visible_text('Tech & Gadgets')
        time.sleep(2)

        #enter the launch date
        Launch_Date=self.driver.find_element(By.NAME,Locatorr.launch_date).send_keys("2021-10-08")

        #enter weblink
        WebLink=(self.driver.find_element(By.ID,Locatorr.weblink))
        WebLink.clear()
        WebLink.send_keys("https://in.pinterest.com/")

        print("image uploaded manually")
        #driver.find_element_by_xpath("//*[@id='account-showcase']/div/div/div[1]/form/fieldset[2]/div/div[1]/div/div").send_keys("C:/Users/ASEEAZ/Desktop/selenuim-python/car.jpg")
        time.sleep(20)

        #click button submit or cancel
        change="no"
        if(change=="yes"):
            submit_button=self.driver.find_element_by_xpath(Locatorr.submit_button).click()
        else:
            CANCEL_button=self.driver.find_element_by_xpath(Locatorr.canc_show).click()

        #comback to previous page
        self.driver.find_element_by_link_text(Locatorr.Dashboard).click()

    def test4_payment_module(self):
        #switvh to payment page by clicking it
        Pay_Page=self.driver.find_element_by_link_text(Locatorr.pay_page).click()
        print("user entered the payment page")

        #click add card button
        AddCard=self.driver.find_element_by_xpath(Locatorr.addcard).click()
        time.sleep(5)
        #click dropdown
        DropDowncre=self.driver.find_element_by_xpath(Locatorr.dropdowncre).click()

        time.sleep(20)
        print("credential entered manually")

        #driver.find_element_by_xpath("//*[@id='credit-card-number']").send_keys(1234567887654321)
        #enter the storebutton
        StoreButton=self.driver.find_element_by_id(Locatorr.storebutton).click()
        time.sleep(10)
        print("button is clicked")

    def tearDown(self):
        print("testcase executed")

    @classmethod
    def tearDownClass(class_name):
        class_name.driver.quit()
        print("compltd")
