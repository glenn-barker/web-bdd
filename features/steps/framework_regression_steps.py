from behave import when, then
from framework import framework_regression


@when("the following steps are executed")
def step_impl(context):
    framework_regression.execute_steps_and_capture_errors(context, context.text)


@then("the above steps should result in the following failure")
def step_impl(context):
    desired_error = context.text.replace("\"\"\"\n", "").strip()
    framework_regression.validate_captured_error_contains(context, desired_error)
