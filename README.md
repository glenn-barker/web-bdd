# web-bdd
This is a simple framework / skeleton project / sample / blueprint / etc. for a web-based behavior-driven development
(BDD) test automation framework in Python.

This is *not* a brand-new implementation of WebDriver or Gherkin. This still uses standard tools like `Selenium`
and `behave` as dependencies for those purposes.

Instead, this project represents how one might organize the numerous components (test cases, test steps, environment
setup, page objects, element locators, explicit waits, etc.) that make up a web-based testing into a simple, easy to
work with and easily extensible framework.

To provide some examples, this project demonstrates each of the above concepts in the context of providing some very
simple web automation around Wikipedia, so you should be able to drill down to see how this Wikipedia automation is
built and jump off from there to write your own web-bdd test automation for whatever platform you need.

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