Feature: Login Action Test
  Description : this feature will test a Login and Logout functionality
  Scenario:Unsuccessful login with invalid credentials
  Given :User is on home page
  When :User navigate to login page
  And :User enters username and password
  And :The user credentials are correct
  Then :User logged on
