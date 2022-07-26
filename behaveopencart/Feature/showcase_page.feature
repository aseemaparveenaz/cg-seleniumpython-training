Feature: The user should be able to perform actions in showcase page in opencart
  Scenario Outline: check showcase page functionality
    Given The user is in the account page for entering into showcase page
    When The user enters the showcase page by clicking the showcase page link
    And The user clicks on the add project button to add projects in show case page
    Then The user enters the <showcase_n> in the showcase name field
    And The user selects the <showcase_typ> from the dropdown list
    When The user enters the <launch_dt> in the date field
    And The user enters the <wb_site> in the website field
    And The user clicks on the submit or cancel button to save or discard the changes given as <this_button> string
    Then The user clicks on the dashboard to come out from showcase page to the account page
    Examples:
      | showcase_n | showcase_typ | launch_dt | wb_site | this_button |
      |CAR         |Tech & Gadgets|2021-10-08 |https://in.pinterest.com/|no|
