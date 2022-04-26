from behave import given, when, then
from time import sleep


@when('Add product to wishlist')
def add_to_wishlist(context):
    context.app.gettop_product_page.hover_product_logo()
    context.app.gettop_product_page.hover_wishlist_icon()
    context.app.gettop_product_page.add_to_wishlist()


@when('Open wishlist page')
def open_wishlist(context):
    context.app.gettop_product_page.open_wishlist()


@then('Verify correct page opens')
def verify_product_page(context):
    context.app.gettop_product_page.verify_product_title()


@then('Verify {product} product page opens')
def verify_correct_product(context, product):
    context.app.gettop_product_page.verify_any_product_title(product)
