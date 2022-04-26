from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class WishlistPage(Page):
    PRODUCT_NAME = (By.CSS_SELECTOR, "td.product-name a[href*='iphone-se']")
    ANY_PRODUCT_NAME = (By.CSS_SELECTOR, "td a[href*='https://gettop.us/product/']")
    REMOVE_PRODUCT = (By.CSS_SELECTOR, ".remove.remove_from_wishlist")
    REMOVED_TEXT = (By.CSS_SELECTOR, 'div.message-container.container')
    SOCIAL_LOGO_LIST = (By.CSS_SELECTOR, '.social-icons.share-icons a')

    def verify_product_present(self):
        # sleep(5)
        self.verify_text("iPhone SE", *self.PRODUCT_NAME)

    def remove_from_wishlist(self):
        self.click(*self.REMOVE_PRODUCT)

    def verify_remove_msg(self):
        self.verify_text("Product successfully removed.", *self.REMOVED_TEXT)

    def wishlist_product_link(self):
        self.click(*self.ANY_PRODUCT_NAME)

    def verify_social_logos(self):
        links = self.find_elements(*self.SOCIAL_LOGO_LIST)
        print(links)
        assert len(links) == 4, f'expected 4 links but instead got {len(links)}'
