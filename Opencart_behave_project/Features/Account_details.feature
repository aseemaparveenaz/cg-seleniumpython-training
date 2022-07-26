Feature: The user should be able to perform actions in account page in opencart
  Scenario: check edit account page functionality
    Given The user is in the account page after entering credentials
    When The user click on the edit account link to enter into edit account page
    Then The user enters the username in username field after entering into edit account page
    And The user enters the firstname in the first name field
    And The user enters the lastname in the last name field
    And The user enters the company name in the company name field
    Then The user enters the taxId in the taxId field
    And The user selects the country from the drop down list
    And The user selects the radio button yes or no for notification preferences
    When The user clicks on the submit or cancel button to save or discard the new information
    Then The user Clicks the Dashboard link to come back to account details page


