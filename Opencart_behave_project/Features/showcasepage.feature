Feature: The user should be able to perform actions in showcase page in opencart
  Scenario: check login functionality

  Scenario: check showcase page functionality
    Given The user is in the account page for entering into showcase page
    When The user enters the showcase page by clicking the showcase page link
    And The user clicks on the add project button to add projects in show case page
    Then The user enters the showcase name in the showcase name field
    And The user selects the showcase type from the dropdown list
    When The user enters the launch date in the date field
    And The user enters the website in the website field
    And The user clicks on the submit or cancel button save or discard the changes
    Then The user clicks on the dashboard to come out from showcase page to the account page