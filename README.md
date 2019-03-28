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

## The Framework
Below is a brief overview of some of the different parts of this framework, including how the code is organized and how
common data structures and references are managed throughout test execution.

### BDD
[behave](https://github.com/behave/behave) is the module this framework uses for its behavior-driven development test
implementation. Be sure to [read the behave docs](https://behave.readthedocs.io/en/latest/) so you know the basics of
how `behave` expects things to be organized and also so you know how to kick off and run your test scenarios.

#### Test Scenarios
Test cases themselves in a BDD framework are always provided as "scenarios" which exist within "features". `behave`
mandates a very specific folder structure that this framework complies with. Every single feature and scenario lives
within the root-level `/features/` directory or any subdirectory therein.

In the examples provided here, you can find two feature files within `/features/wikipedia_features/`. Each
of these feature files contains one-or-more scenarios that correspond to the actual test cases that are executed when
you run tests with `behave`.

>As a best practice, your test suites should be logically divided into broad feature areas, with each feature containing
specific granular scenarios that represent specific use cases or key areas of functionality. The steps within a
scenario should be written in a high-level language that does not get overly bogged down in technical details.

#### Step Definitions
Every step of a test scenario begins with `Given`, `When`, or `Then`. (Some additional keywords like `And` & `But`
are also available which are syntactic sugar provided to make the written scenarios "flow" better when read by a human.)

The code that is actually executed for each step is declared in a step definitions module. `behave` is rather strict
in this regard and mandates that all step definitions exist *directly* under the `/features/steps/` directory. Unlike
with feature files, step definitions *cannot* exist within deeper subdirectories.

If you look within the `/features/steps/` directory you will see two `wikipedia_*_steps.py` modules which contain all
of the step definitions used for the two example Wikipedia feature files.

>As a best practice, step definitions should be written as concisely as possible, ideally containing nothing more than
simple class instantiations and function calls. Complex test and functional logic should not be written directly within
the step definition and should instead be abstracted away.

#### Test Setup and Fixtures
The `/features/environment.py` module should contain all of the setup and teardown logic that needs to execute for
the test framework. Things such as creating/destroying web browser instances, reading config files, generating mock
test data, etc. should be defined here.

[fixtures](https://behave.readthedocs.io/en/latest/fixtures.html) are used for this process, and they can either be
coded to always be used or to only be used when certain `@tags` are specified within the test scenarios or features.
In this example framework, the logic for constructing and destroying a web browser instance using `Selenium` is
activated by tagging any scenario or feature with the `@fixture.browser` tag, and this logic is defined here.

#### Framework Regression
Frankly, it's not enough to just write some functional automation logic for your steps and call it a day. An automation
framework is only as good as the failures it generates - a test case that passes 100% of the time is worthless!

It's important to test the tests. As you write your verifications & asserts in your `Then` steps, you should write
test scenarios against your own code to verify that your test logic can fail and throw errors under the appropriate
circumstances.

A few steps and some use case examples have already been provided around this area.
`/features/framework_regression_features/` contains a single feature file with some scenarios that intentionally
"incorrect" results so that we can verify that our tests generate proper test failures. A few special step definitions
are used to capture and validate the assertion errors thrown by arbitrary scenarios, and you can find the appropriate
step definitions under the `/features/steps/` directory.

### Selenium
[Selenium WebDriver](https://pypi.org/project/selenium/) is the module used for browser UI automation. As mentioned
earlier, you will need to download the web drivers for your specific browser choice(s) yourself and ensure they are
available in your `PATH` environment variable.

#### Browser Instantiation and Teardown
As listed above, all setup & teardown logic should happen in the `/features/environment.py` module using test
`fixtures`.

When the browser window is created, a reference is stored in the scenario's `context` which is globally accessible
across all step definitions. Also note that in this framework, rather than storing the Selenium `driver` reference
directly, we create and store a new `SeleniumWrapper` object and pass that around via `context.selenium`. The
`SeleniumWrapper` contains a reference to the underlying Selenium `driver` but also contains a number of other helpful
fields and functions which are described later.

In this example framework, browser [fixtures](https://behave.readthedocs.io/en/latest/fixtures.html) are controlled
via the `@fixture.browser` tag in your scenarios or features. In an automation framework where you may have a mixture
of UI (Selenium browser) and non-UI (API / DB / etc.) tests, it probably makes sense to use this kind of mechanism of
allowing `@fixture` tags to control the browser usage. In a pure UI automation framework that *only* contains Selenium
tests, it is probably redundant to be forced to include this type of tag everywhere, so you may instead modify
`/features/environment.py` to just always use a browser fixture at the start of every scenario or feature.

#### Page Object Model and Element Locators
Page Object Model (POM) is a design pattern for UI automation where you define classes/objects for key pages and
controls that contain functions for any type of operation a user would perform with that page or control.

A few examples are provided under `/pages/wikipedia_pages/`. Note how a class is defined for each page, and each class
contains the relevant types of actions or information you need to perform on that page.

In this framework, each page object is a child of the basic `Page` class defined in `/pages/page.py`, which is a very
simple class that merely keeps a reference to the `SeleniumWrapper` object that was passed in during instantiation. In
this way, you can code your BDD step definitions to construct page objects, pass in the `context.selenium` reference
that was instantiated during the test startup in `/features/environment.py`, and then every child page object that you
define will have a reference to the appropriate `SeleniumWrapper` object.

It's also a good practice to keep all of your locators (XPath, CSS selectors, etc.) for a given page object in one
organized place, rather than strewn throughout the class. Each of the examples provided here show one way you can go
about creating a simple subclass to contain the locator definitions underneath each page object class so that they
can be referenced as needed.

---

Contrary to the name, page objects do not only have to be created for full pages. It is also useful to define page
objects for individual elements or controls that exist within a page. Some examples are provided in
`/pages/wikipedia_controls/`. Obviously you don't need to do this in every case - for instance, a simple login page
that only contains two text fields and a button probably doesn't need individual page objects created for each field.
But in some cases, it is useful to split out certain elements or controls into their own page objects.

One good reason to do this is for shared controls that can exist on multiple pages. For instance, on Wikipedia, the
home page as well as every individual article page all contain a search bar. Rather than defining the exact same type
of search bar across both page objects, it's easier and more efficient to create a single page object just for the
search control that can work across pages.

Another good reason is if the control in question is of sufficient complexity that putting all of the logic within a
single page object class would make the code difficult to work with. For instance, the categories box that appears at
the bottom of each Wikipedia article has some additional complexity over a normal web element that requires some
additional functionality to be able to locate the main container and parse out the individual links within. While we
could define all of this functionality just within the `ArticlePage`, it might make sense to break it out into its own
class.

There is some subjectivity here and it's up to you as to whether you prefer very large page objects that fully
encapsulate the implementation of all complex controls contained within, or whether you prefer smaller page objects
with specific implementation details of complex controls elsewhere.

#### Explicit Waits
Waits are used in any UI automation to increase overall stability and to reduce the brittleness of your test. Rather
than failing a test if an element cannot be found right away, it's better to provide the ability to wait for an
element in case it takes some time to load or to become available. (On the flip side, you do *not* want to use
hard coded sleeps as this introduces unnecessary slowness and wait time into your automation.)

`Selenium` already provides a `wait` mechanism along with some expected conditions, but as you find yourself coding
the same boilerplate code to create these `wait` objects and pass in the appropriate timeouts over and over again,
support for this has been rolled into the `SeleniumWrapper` class. If you need access to a `wait` object, simply
reference the `wait` or `load_wait` (the former for shorter waits where it's generally expected that the page is
already loaded and in a ready state, the latter when the page may still be loading and a longer timeout is desired)
attributes from the `selenium` attribute that every page object has access to.

Even better, the logic for using `wait` and the expected conditions to verify that an element is visible and ready to
be interacted with has also been rolled into `SeleniumWrapper`. Simply call `find_visible_element(by)` and all of the
logic of using explicit waits, expected conditions, and returning the element reference will already be handled for
you. 
