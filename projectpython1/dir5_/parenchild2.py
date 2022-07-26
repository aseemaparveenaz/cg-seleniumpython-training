from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

email_element = driver.find_elements_by_xpath("//input[@type = 'text' and @id = 'userEmail']//ancestor::*")
for i in email_element:
    ancestor_class = i.get_attribute("class")
    if ancestor_class == "":
        ancestor_id = i.get_attribute("id")
        if ancestor_id == "":
            print("Ancestor Tag of Email: ", i.tag_name)
        else:
            print("Ancestor ID of Email: ", ancestor_id)
    else:
        print("Ancestor class of Email : ", ancestor_class)

driver.close()