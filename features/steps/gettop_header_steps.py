from behave import given, when, then


@given('Open GetTop home page')
def open_gettop(context):
    context.app.gettop_header.open_gettop_main()


@when('Hover over product category')
def hover_product_category(context):
    context.app.gettop_header.hover_product_category()


@when('Hover over categories')
def hover_categories(context):
    context.app.gettop_header.hover_all_product_categories()


@when('Verify 4 links present')
def link_verification(context):
    context.app.gettop_header.verify_number_links()


@when('Hover over {category} category')
def category_hover(context, category):
    context.app.gettop_header.dynamic_hover_category(category)


@when('Hover over dropdown menu {product}')
def dropdown_product_hover(context, product):
    context.app.gettop_header.dynamic_hover_product(product)


@when('Verify correct {item_number} is present')
def verify_dropdown_product(context, item_number):
    context.app.gettop_header.verify_menu_product(item_number)


@then('Click products and verify correct pages open')
def click_verify(context):
    context.app.gettop_header.click_and_verify()


@then('Verify that {product_name} present')
def verify_dropdown_products(context, product_name):
    context.app.gettop_header.verify_menu_link_product(product_name)


@then('Click category links and verify correct page opens')
def click_verify(context):
    context.app.gettop_header.click_category_and_verify_url()
    # context.app.gettop_header.click_category_verify_page()
