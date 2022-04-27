from behave import given, when, then


@given('Open GetTop home page')
def open_gettop(context):
    context.app.gettop_header.open_gettop_main()


@when('Hover over product category')
def hover_product_category(context):
    context.app.gettop_header.hover_product_category()


@when('Verify 4 links present')
def link_verification(context):
    context.app.gettop_header.verify_number_links()


@then('Click products and verify correct pages open')
def click_verify(context):
    context.app.gettop_header.click_and_verify()
