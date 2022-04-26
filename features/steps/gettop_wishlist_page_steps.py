from behave import given, when, then


@then('Verify iPhone SE added to wishlist')
def verify_product(context):
    context.app.gettop_wishlist_page.verify_product_present()


@then('Remove product from wishlist')
def remove_product(context):
    context.app.gettop_wishlist_page.remove_from_wishlist()


@then('Verify removal message')
def verify_removal(context):
    context.app.gettop_wishlist_page.verify_remove_msg()


@when('Click product item link in wishlist')
def click_wishlist_product(context):
    context.app.gettop_wishlist_page.wishlist_product_link()


@then('Verify social media logos present')
def wishlist_social_logos(context):
    context.app.gettop_wishlist_page.verify_social_logos()
