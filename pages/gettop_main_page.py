from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class MainPage(Page):
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a[href*='product-category/iphone/']")
    PRODUCT_LINK = (By.ID, 'menu-item-381')

    def open_gettop_main(self):
        self.open_page()

    def hover_product_category(self):
        tab = self.find_element(*self.PRODUCT_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()

    def click_product_link(self):
        self.click(*self.PRODUCT_LINK)

    def open_product_page(self, product_id):
        self.gettop_open_product_page(product_id)
