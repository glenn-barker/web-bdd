from behave import given, when, then
from pages.wikipedia_pages.home_page import HomePage
from pages.wikipedia_controls.search_control import SearchControl


@given(u'the Wikipedia homepage is open')
def step_impl(context):
    home_page = HomePage(context.selenium)
    home_page.visit()


@when(u'the user searches Wikipedia for: {search_term}')
def step_impl(context, search_term):
    search_control = SearchControl(context.selenium)
    search_control.search(search_term)
