Feature: The user should be able to perform actions in payment page in opencart
    Scenario: check change password functionality
    Given The user is in the account page for entering into change password page
      When The user enters the change password link to enter into payment page
      And The user enters the old password in the old password field
      And The user enters the new password in the new password field
      And The user enters the new password again in the confirm password field
      And The user clicks the submit or cancel button to change the password or to discard the changes
      Then The user come back from change password page to account page by clicking dashboard
