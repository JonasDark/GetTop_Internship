from pages.gettop_main_page import MainPage
from pages.gettop_product_page import ProductPage
from pages.gettop_wishlist_page import WishlistPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.gettop_main_page = MainPage(self.driver)
        self.gettop_product_page = ProductPage(self.driver)
        self.gettop_wishlist_page = WishlistPage(self.driver)
