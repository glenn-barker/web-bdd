def execute_steps_and_capture_errors(context, steps_text):
    context.captured_assertion_error = None

    try:
        context.execute_steps(steps_text)
    except AssertionError as captured_error:
        context.captured_assertion_error = str(captured_error)


def validate_captured_error_contains(context, desired_error):
    captured_error = context.captured_assertion_error

    assert captured_error is not None, f"No error was captured when \"{desired_error}\" was expected!"
    assert desired_error in captured_error, \
        f"The captured error did not contain \"{desired_error}\" but instead: \n---\n{captured_error}\n---"
