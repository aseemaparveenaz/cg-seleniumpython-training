Feature: Get attribute of Username and Verify Heading
  Scenario: Test Get attribute and Verify Heading
    Given user is on home page
    Then heading should be "Please identify yourself"
    Then attribute of username should be printed