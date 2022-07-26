Feature: The user should be able to perform actions in account page in opencart
  Scenario Outline: check edit account page functionality
    Given The user is in the account page after entering credentials
    When The user click on the edit account link to enter into edit account page
    Then The user enters the <user_n> in username field after entering into edit account page
    And The user enters the <first_n> in the first name field
    And The user enters the <last_n> in the last name field
    And The user enters the <company_n> in the company name field
    Then The user enters the <tax_Id> in the taxId field
    And The user enters the <e_mail> in the email field
    And The user selects the <country_n> from the drop down list
    And The user selects the radio button yes or no for notification preferences given in <radio_str>
    When The user clicks on the submit or cancel button to save or discard the new information given as <click_btn>
    Then The user Clicks the Dashboard link to come back to account details page from edit account page
    Examples:
      |user_n| first_n | last_n | company_n | tax_Id | e_mail |country_n | radio_str | click_btn |
      |Aseema_parveen | aseema | AZ | capgemini | nil | aseemaparveenaz@gmail.com |99 | no  | yes |
      |Aseema         |parveen |AZ  | capg      | 745 | aseemaparveensha@gmail.com | 98 | yes |no |


