@fixture.browser @wikipedia @article
Feature: Wikipedia Article Functionality
  As an automation engineer,
  In order to demonstrate basic BDD automation practices with Behave + Selenium,
  I want to be able to implement and execute some simple web automation against Wikipedia


  Background: Wikipedia is open
    Given the Wikipedia homepage is open


  Scenario: Clicking the first link on an article takes you to a similar article
    When the user searches Wikipedia for: Python (programming language)
    And the first link in the Wikipedia article is clicked
    Then the Interpreted language Wikipedia page should be open


  Scenario: Articles contain clickable links to relevant categories
    When the user searches Wikipedia for: Test automation
    Then the following Wikipedia categories should be available:
      | Category         |
      | Software testing |
      | Automation       |
    When the Automation category link is clicked
    Then the Category:Automation Wikipedia page should be open
