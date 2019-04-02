import json
from behave.fixture import use_fixture_by_tag
from features.fixtures import selenium_fixtures


# Map each valid `@fixture` tag with the appropriate test fixture.
fixture_registry = {}
fixture_registry.update(selenium_fixtures.fixture_registry)


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
