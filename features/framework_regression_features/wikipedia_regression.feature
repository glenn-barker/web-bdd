@fixture.browser @wikipedia @automation_regression
Feature: Wikipedia Regression
  As an automation engineer,
  In order to maintain a quality automation framework
  I want to verify that all of my assertions are valid and that test failures are properly generated

  In this case, I want to specifically verify that my Wikipedia automation validations are accurate


  Background: Wikipedia is open
    Given the Wikipedia homepage is open


  Scenario: Article page title verification catches when the article title does not match the expected value
    When the following steps are executed:
      """
      When the user searches Wikipedia for: Star Trek
      Then the Star Wars Wikipedia page should be open
      """
    Then the above steps should result in the following failure:
      """
      The Star Trek article is open instead of Star Wars
      """


  Scenario: Article category verification catches when expected categories do not exist
    When the following steps are executed:
      """
      When the user searches Wikipedia for: United States
      Then the following Wikipedia categories should be available:
      | Category                   |
      | Countries in North America |
      | Scandinavian countries     |
      | Countries in Europe        |
      """
    Then the above steps should result in the following failure:
      """
      The following expected article categories are missing: Scandinavian countries, Countries in Europe
      """