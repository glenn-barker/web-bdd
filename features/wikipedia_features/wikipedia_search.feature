@fixture.browser
Feature: Wikipedia Search Functionality
  As an automation engineer,
  In order to demonstrate basic BDD automation practices with Behave + Selenium,
  I want to be able to implement and execute some simple web automation against Wikipedia


  Background: Wikipedia is open
    Given the Wikipedia homepage is open


  Scenario: Searching for an article based on an exact name will open that article
    When the user searches Wikipedia for: Cucumber (software)
    Then the Cucumber (software) Wikipedia page should be open


  Scenario: Searching for an article based on a shorter name will redirect to the full article title
    When the user searches Wikipedia for: python language
    Then the Python (programming language) Wikipedia page should be open


  Scenario: Searching for an article that does not exist returns generic search results
    When the user searches Wikipedia for: this page does not exist
    Then the Search results Wikipedia page should be open
