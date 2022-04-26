from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class ProductPage(Page):
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "div.product-images")
    HEART_ICON = (By.CSS_SELECTOR, 'i.icon-heart')
    PRODUCT_PAGE_TITLE = (By.CSS_SELECTOR, 'h1.product-title.entry-title')

    def hover_product_logo(self):
        tab = self.find_element(*self.PRODUCT_IMAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()

    def hover_wishlist_icon(self):
        tab = self.find_element(*self.HEART_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()

    def add_to_wishlist(self):
        self.click(*self.HEART_ICON)

    def open_wishlist(self):
        self.click(*self.HEART_ICON)

    def verify_product_title(self):
        self.verify_text("iPhone SE", *self.PRODUCT_PAGE_TITLE)

    def verify_any_product_title(self, product):
        self.verify_partial_text(product, *self.PRODUCT_PAGE_TITLE)

