import json
from behave import fixture
from behave.fixture import use_fixture_by_tag
from features.fixtures import selenium_fixtures


@fixture
def selenium_browser(context):
    # Using the `fixture.browser` fixture should do a lookup on the config and return an appropriate
    # sub-fixture, e.g.: `fixture.browser.chrome`.
    browser = context.config.userdata.get("browser", "chrome").lower()
    fixture_tag = f"fixture.browser.{browser}"
    try:
        yield use_fixture_by_tag(fixture_tag, context, fixture_registry)
    except LookupError:
        raise ValueError(f"Unsupported browser option: {browser}")


fixture_registry = {
    # Map each valid `@fixture` tag with the appropriate test fixture.
    "fixture.browser": selenium_browser,
    "fixture.browser.chrome": selenium_fixtures.chrome,
    "fixture.browser.edge": selenium_fixtures.edge,
    "fixture.browser.firefox": selenium_fixtures.firefox,
    "fixture.browser.ie": selenium_fixtures.ie,
    "fixture.browser.safari": selenium_fixtures.safari,
}


def before_all(context):
    # Load and update settings from JSON config file.
    # Note that all of the options provided in the config.json can also be provided as cmd line params to
    # override the defaults specified in the config.
    with open("config.json") as json_file:
        json_data = json.load(json_file)

    context.config.update_userdata(json_data)


def before_tag(context, tag):
    # `@fixture` tags can be used to enable fixtures like web browsers and other resources required throughout the test.
    if tag.startswith("fixture."):
        return use_fixture_by_tag(tag, context, fixture_registry)
