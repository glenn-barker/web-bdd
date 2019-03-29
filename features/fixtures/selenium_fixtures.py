from behave import fixture
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from framework.selenium_helpers.selenium_wrapper import SeleniumWrapper


@fixture
def chrome(context):
    # -- FIXTURE SETUP
    try:
        chrome_options = ChromeOptions()

        if should_use_headless(context):
            chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(chrome_options=chrome_options)
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium.driver
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Chrome!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def edge(context):
    # -- FIXTURE SETUP
    try:
        context.selenium = SeleniumWrapper(context, webdriver.Edge())
        yield context.selenium.driver
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Edge!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def firefox(context):
    # -- FIXTURE SETUP
    try:
        firefox_options = FirefoxOptions()

        firefox_options.headless = should_use_headless(context)

        driver = webdriver.Firefox(options=FirefoxOptions)
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium.driver
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Firefox!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def ie(context):
    # -- FIXTURE SETUP
    try:
        ie_options = IEOptions()

        if should_use_headless(context):
            print("WARNING: Current config asks for both headless execution and IE execution, which are incompatible.")

        driver = webdriver.Ie(ie_options=ie_options)
        context.selenium = SeleniumWrapper(context, driver)
        yield context.selenium.driver
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing IE!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


@fixture
def safari(context):
    # -- FIXTURE SETUP
    try:
        context.selenium = SeleniumWrapper(context, webdriver.Safari())
        yield context.selenium.driver
    except WebDriverException as e:
        print("Selenium WebDriverException raised when initializing Safari!")
        raise e
    # -- FIXTURE CLEANUP
    context.selenium.driver.quit()


def should_use_headless(context):
    return context.config.userdata.getbool("headless", False)
