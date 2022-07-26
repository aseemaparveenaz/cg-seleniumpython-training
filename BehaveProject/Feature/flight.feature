Feature: The user can book available flights
  Scenario: The user can find a flight from Paris to London
    Given the user is on the search page
    When the user selects Paris as a departure city
    And the user selects London as a destination city
    And clicks on the Find Flights button
    Then flights are presented on the search result page