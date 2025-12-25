Feature: Login
  Scenario: Successful login
    Given user opens login page
    When user logs in with valid credentials
    Then user should see the secure area
