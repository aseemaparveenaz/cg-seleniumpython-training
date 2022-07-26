Feature: The user should be able to perform actions in payment page in opencart
  Scenario: Check payment page functionality
    Given The user is in Account page to enter into payment page
    When The user click on the payment page link to move to payment page
    And The user click on Add payment method button to store the card
    And The user select the credit card option from the dropdown
    Then The user click on store card button to save the credit card
