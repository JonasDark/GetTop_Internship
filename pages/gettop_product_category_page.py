from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class GettopProductCategory(Page):
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, 'div.product div.col-inner div.box div.box-text div.title-wrapper p.category')
    ALL_PRODUCTS = (By.CSS_SELECTOR, 'div.products div.product')
    SHOWING_RESULTS = (By.CSS_SELECTOR, 'div.medium-text-center p.hide-for-medium')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.products div.product div.col-inner div.box div.box-text div.title-wrapper '
                                     'p.name')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.product div.col-inner div.box div.box-text div.price-wrapper '
                                      'span.price')
    QUICKVIEW = (By.CSS_SELECTOR, 'div.box-image div.grid-tools a')
    QUICKVIEW_X = (By.CSS_SELECTOR, 'body.archive div.mfp-ready button.mfp-close')
    ADD_CART_BTN = (By.CSS_SELECTOR, 'div.product-lightbox-inner form.cart button.button')
    CART_NUMBER_ITEMS = (By.CSS_SELECTOR, "a[href*='cart'] span.cart-icon strong")

    def open_close_quickview(self):
        bat = self.find_elements(*self.QUICKVIEW)
        for i in range(len(bat)):
            tab = bat[i]
            actions = ActionChains(self.driver)
            actions.move_to_element(tab)
            actions.perform()
            tab.click()
            # sleep(1)
            self.find_element(*self.ADD_CART_BTN)
            # sleep(1)
            self.click(*self.QUICKVIEW_X)
            # sleep(1)

    def open_quickview_add_cart(self):
        bat = self.find_elements(*self.QUICKVIEW)
        for i in range(len(bat)):
            bat = self.find_elements(*self.QUICKVIEW)
            tab = bat[i]
            actions = ActionChains(self.driver)
            actions.move_to_element(tab)
            actions.perform()
            tab.click()
            # sleep(1)
            self.find_element(*self.ADD_CART_BTN)
            # sleep(1)
            self.click(*self.ADD_CART_BTN)
            # sleep(1)

    def open_product_category_page(self, product):
        self.gettop_open_category_page(product)

    def verify_cart_product_amount(self):
        products = self.driver.find_elements(*self.ALL_PRODUCTS)
        page_products = len(products)
        actual_text = self.driver.find_element(*self.CART_NUMBER_ITEMS).text
        assert str(page_products) in actual_text, \
            f'Expected text {page_products} is not in {actual_text}'

    def verify_cat_text(self, cat):
        # self.verify_text(cat, *self.PRODUCT_CATEGORY)
        actual_word = self.driver.find_elements(*self.ALL_PRODUCTS)

        for i in actual_word:
            assert f'{cat}' in i.text, f'Expected the word {cat} in element'
            product_cat = i.find_element(*self.PRODUCT_CATEGORY).text
            print(product_cat)
            assert product_cat, 'Expected product name text in element'

    def verify_number_products(self):
        products = self.driver.find_elements(*self.ALL_PRODUCTS)
        print(products)
        page_products = len(products)  # this is our expected number
        print(page_products)
        actual_text = self.driver.find_element(*self.SHOWING_RESULTS).text
        assert str(page_products) in actual_text, \
            f'Expected text {page_products} is not in {actual_text}'

    def verify_product_category_label(self):
        all_products = self.find_elements(*self.ALL_PRODUCTS)
        category = self.find_element(*self.PRODUCT_CATEGORY)
        for i in range(len(all_products)):
            self.find_elements(*self.PRODUCT_CATEGORY)
            category = self.find_elements(*self.PRODUCT_CATEGORY)
            print(category[i].text)
        assert len(all_products) == len(category), 'amount of products and amount of product names do not match'

    def verify_product_cat_name_price(self):
        all_products = self.find_elements(*self.ALL_PRODUCTS)
        for i in range(len(all_products)):
            self.verify_product_category_label()
            self.verify_product_name_label()
            self.verify_product_price_label()

    def verify_product_name_label(self):
        all_products = self.find_elements(*self.ALL_PRODUCTS)
        name = self.find_element(*self.PRODUCT_NAME)
        for i in range(len(all_products)):
            self.find_elements(*self.PRODUCT_NAME)
            name = self.find_elements(*self.PRODUCT_NAME)
            print(name[i].text)
        assert len(all_products) == len(name), 'amount of products and amount of product names do not match'

    def verify_product_price_label(self):
        all_products = self.find_elements(*self.ALL_PRODUCTS)
        price = self.find_elements(*self.PRODUCT_PRICE)
        for i in range(len(all_products)):
            self.find_elements(*self.PRODUCT_PRICE)
            price = self.find_elements(*self.PRODUCT_PRICE)
            print(price[i].text)
        assert len(all_products) == len(price), 'amount of products and amount of product prices do not match'
