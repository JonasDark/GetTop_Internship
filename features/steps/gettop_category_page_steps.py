from behave import given, when, then


@given('Open {category} category page')
def open_category(context, category):
    context.app.gettop_product_category_page.open_product_category_page(category)


@when('Open quickview for each product on page and add to cart')
def quickview_add_cart(context):
    context.app.gettop_product_category_page.open_quickview_add_cart()


@then('Verify only {category} category products are displayed')
def verify_product_category(context, category):
    context.app.gettop_product_category_page.verify_cat_text(category)


@then('Verify amount of products displayed matches showing result digit')
def verify_number_products_present(context):
    context.app.gettop_product_category_page.verify_number_products()


@then('verify product category label present')
def verify_category_label(context):
    context.app.gettop_product_category_page.verify_product_category_label()


@then('Verify product name present')
def verify_product_name_label(context):
    context.app.gettop_product_category_page.verify_product_name_label()


@then('Verify product price present')
def verify_product_price_label(context):
    context.app.gettop_product_category_page.verify_product_price_label()


@then('Verify product has a category, name, and price')
def verify_all_three(context):
    context.app.gettop_product_category_page.verify_product_cat_name_price()


@then('Open and close quickview for each product on page')
def quickview_open(context):
    context.app.gettop_product_category_page.open_close_quickview()


@then('verify correct number of items added to cart')
def number_cart(context):
    context.app.gettop_product_category_page.verify_cart_product_amount()
