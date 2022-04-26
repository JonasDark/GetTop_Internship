from behave import given, when, then
from time import sleep


@given('Open GetTop main page')
def open_gettop(context):
    context.app.gettop_main_page.open_gettop_main()


@given('Open GetTop {product_id} product page')
def open_gettop_product(context, product_id):
    context.app.gettop_main_page.open_product_page(product_id)


@when('Open iPhone SE product page')
def click_product_link(context):
    context.app.gettop_main_page.hover_product_category()
    context.app.gettop_main_page.click_product_link()
