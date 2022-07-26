Feature:User information
  Scenario Outline:Check login functionality
    Given user launch browser
    When user open rediff
    And user enter <name> and <password>
    And user clicks on login
    Then user should be able to logged in
    Examples: Credentials
      |  name | password|
      | user1 | pwd1    |
      | user2 | pwd2    |