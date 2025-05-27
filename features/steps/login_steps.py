from behave import given, when, then

@given('the user is on the login page')
def step_given_user_on_login_page(context):
    # Simulate user navigating to login page
    context.on_login_page = True

@when('they enter valid credentials')
def step_when_enter_credentials(context):
    if context.on_login_page:
        # Simulate credentials verification
        context.login_success = True

@then('they should be redirected to the dashboard')
def step_then_redirect_to_dashboard(context):
    assert context.login_success is True, "Login failed; user not redirected"
