Feature: Register
  Scenario: user register at Register page
    Given user navigate to page and click register
    Then user should be navigated to Register page
    When user enter new credential and press enter
    Then user should be navigated back to home page
    When user click add to cart iphone and headphone on homepage
    Then cart logo should increase along with the number of clicks
    When user click cart logo on the top right corner
    Then user should be navigated to cart page
