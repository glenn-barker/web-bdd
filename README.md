# web-bdd
This is a simple framework / skeleton project / sample / blueprint / etc. for a web-based behavior-driven development
(BDD) test automation framework in Python, powered by [behave](https://github.com/behave/behave),
[Selenium](https://pypi.org/project/selenium/), and [requests](https://github.com/kennethreitz/requests).

Essentially this project demonstrates how one might structure and organize a framework that utilizes these libraries
and deals with common design patterns and solutions, such as the layout of page objects and locators, dealing with
explicit waits, and creating scalable CI-ready test automation.

To provide some examples, this project demonstrates each of the above concepts in the context of providing some very
simple web automation around Wikipedia, so you should be able to drill down to see how this Wikipedia automation is
built and jump off from there to write your own web-bdd test automation for whatever platform you need.

## Progress:
Areas that have been covered so far:
* Basic folder structure for BDD. (features / scenarios / step definition implementations)
* Basic folder structure for POM. (pages, controls, and locators)
* Setup / teardown hooks for instantiating Selenium browser instances using test fixtures.
* Cross-browser support with options tailored to each (e.g. optional headless execution for all browsers that support
  it.)
* Other misc. Selenium "quality of life" enhancements, such as managing explicit waits, expanded the "expected
  conditions" library (search for elements by locator, returning only those that are actually visible), etc., all
  provided in a wrapper class that every page object has access to.
* Test settings (browser selection, etc.) using config file, with the option to override defaults provided in the
  config by passing in cmd line args.
* Demo of all of the above with some simple examples demonstrating working web automation with Wikipedia as the
  application under test.
* Parallel execution. (See [Parallel Execution](https://github.com/glenn-barker/web-bdd/wiki/Parallel-Execution) on the
  Wiki for info on setting this up.)

Areas that are yet to be covered:
* Remote execution. (Selenium Grid)
* Demonstration of test results reporting. (Cucumber reports)
* Logging info / warnings / errors during test execution.
* API testing examples using `requests`.

## Pre-requisites
1. Python 3.7
2. `pip install pipenv` for package installation and virtual environment management.
3. Currently, the web drivers required by Selenium (e.g. `chromedriver.exe`) are not packaged or included here,
   so you will need to provide these yourself and ensure they are in a location that is accessible. (I.E.
   they are in your `PATH`.)
   
   You can download the latest web drivers yourself:
   * Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads
   * Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
   * Firefox: https://github.com/mozilla/geckodriver/releases
   * Internet Explorer: https://www.seleniumhq.org/download/
   * Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/

## Install
```
$ git clone https://github.com/glenn-barker/web-bdd.git
$ cd web-bdd
$ pipenv install
```

## Running
Kick off the sample web automation provided:

`$ pipenv run behave`

You should see a Chrome browser open up, navigate around Wikipedia, and close. This process will repeat a few times as
each test feature is iterated through, and the final test summary will be displayed at the end.

## Documentation
Need more info? [Check the Wiki.](https://github.com/glenn-barker/web-bdd/wiki)