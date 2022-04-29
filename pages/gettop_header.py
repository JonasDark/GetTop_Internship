from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class GettopHeader(Page):
    CLICKABLE_CATEGORIES = (By.CSS_SELECTOR, 'ul.header-nav li.menu-item.has-dropdown')
    IPHONE_PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a[href*='product-category/iphone/']")
    IPAD_PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a[href*='product-category/ipad/']")
    IPHONE_EXPECTED_NAMES = ['iPhone 12', 'iPhone 11', 'iPhone 11 Pro', 'iPhone SE']
    IPAD_EXPECTED_NAMES = ['iPad', 'iPad Pro', 'iPad mini', 'iPad Air']
    CAT_EXPECTED_NAMES = ['macbook', 'iphone', 'ipad', 'watch', 'airpods']
    CURRENT_PAGE = (By.CSS_SELECTOR, 'h1.product-title')
    CURRENT_CAT_PAGE = (By.CSS_SELECTOR, 'div.page-title div.flex-row div.flex-grow div nav.uppercase')
    IPHONE_CLICKABLE_LINKS = (By.CSS_SELECTOR, "li#menu-item-469 ul.sub-menu li")
    IPAD_CLICKABLE_LINKS = (By.CSS_SELECTOR, "li#menu-item-470 ul.sub-menu li a")
    ALL_DROPDOWN_PRODUCTS = (By.CSS_SELECTOR, 'ul.sub-menu.nav-dropdown li')
    ALL_EXPECTED_NAMES = ['MacBook Pro 13-inch', 'MacBook Pro 16-inch', 'MacBook Air','iPhone 12', 'iPhone 11',
                          'iPhone 11 Pro', 'iPhone SE', 'iPad', 'iPad Pro', 'iPad mini', 'iPad Air', 'Watch Series 5',
                          'Watch Series 3', 'Cases & protection', 'AirPods with Wireless Charging Case',
                          'AirPods Pro']
    DYNAMIC_PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a[href*='product-category/{CATEGORY}/']")
    DYNAMIC_CLICKABLE_LINKS = (By.CSS_SELECTOR, 'ul.sub-menu.nav-dropdown li#menu-item-{MENU_ITEM_NUMBER}')
    EXPERIMENT = (By.CSS_SELECTOR, "ul.sub-menu.nav-dropdown li a[href*='{PRODUCT_NAME}']")

    def click_and_verify(self):
        click_link = self.driver.find_elements(*self.IPHONE_CLICKABLE_LINKS)
        for i in range(len(click_link)):
            self.hover_product_category()
            click_link = self.driver.find_elements(*self.IPHONE_CLICKABLE_LINKS)
            click_link[i].click()
            current_page = self.driver.find_element(*self.CURRENT_PAGE).text
            assert current_page == self.IPHONE_EXPECTED_NAMES[i], 'Text not expected'
            if current_page == self.IPHONE_EXPECTED_NAMES[-1]:
                print('Success!!!')

    def click_category_and_verify_url(self):
        click_cat = self.driver.find_elements(*self.CLICKABLE_CATEGORIES)
        for i in range(len(click_cat)):
            # self.hover_product_category()
            click_cat = self.driver.find_elements(*self.CLICKABLE_CATEGORIES)
            click_cat[i].click()
            cat_list = self.CAT_EXPECTED_NAMES
            for j in range(len(cat_list)):
                cat_list = self.CAT_EXPECTED_NAMES
                self.verify_url_contains_query(cat_list[i])

    def click_category_verify_page(self):
        click_category = self.driver.find_elements(*self.CLICKABLE_CATEGORIES)
        for i in range(len(click_category)):
            # self.hover_product_category()
            click_category = self.driver.find_elements(*self.CLICKABLE_CATEGORIES)
            click_category[i].click()
            current_page = self.driver.find_element(*self.CURRENT_CAT_PAGE).text
            assert current_page == self.CAT_EXPECTED_NAMES[i], 'Text not expected'
            if current_page == self.CAT_EXPECTED_NAMES[-1]:
                print('Success!!!')

    def dynamic_hover_category(self, product):
        product_locator = self._get_product_locator(product)
        tab = self.find_element(*product_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()
        #sleep(3)

    def dynamic_hover_product(self, product):
        product_dropdown_locator = self._get_product_link_locator(product)
        tab = self.find_element(*product_dropdown_locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()
        #sleep(3)

    def _get_product_verifi_locator(self, product: str):
        return[self.EXPERIMENT[0], self.EXPERIMENT[1].replace('{PRODUCT_NAME}', product)]

    def _get_product_verification_locator(self, product: str):
        return[self.DYNAMIC_CLICKABLE_LINKS[0], self.DYNAMIC_CLICKABLE_LINKS[1].replace('{MENU_ITEM_NUMBER}', product)]

    def _get_product_locator(self, product: str):
        return[self.DYNAMIC_PRODUCT_CATEGORY[0], self.DYNAMIC_PRODUCT_CATEGORY[1].replace('{CATEGORY}', product)]

    def _get_product_link_locator(self, product: str):
        return [self.EXPERIMENT[0], self.EXPERIMENT[1].replace('{PRODUCT_NAME}', product)]

    def hover_product_category(self):
        tab = self.find_element(*self.IPHONE_PRODUCT_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()

    def open_gettop_main(self):
        self.open_page()

    def verify_correct_product(self, product):
        product_locator = self._get_product_locator(product)
        self.wait_for_element_appear(*product_locator)

    def verify_menu_link_product(self, product):
        product_v_locator = self._get_product_verifi_locator(product)
        self.wait_for_element_appear(*product_v_locator)

    def verify_menu_product(self, product):
        product_v_locator = self._get_product_verification_locator(product)
        self.wait_for_element_appear(*product_v_locator)

    def verify_menu_products(self):
        verify_link = self.driver.find_elements(*self.IPAD_CLICKABLE_LINKS)
        for i in range(len(verify_link)):
            self.hover_product_category()
            verify_link = self.driver.find_element(*self.IPAD_CLICKABLE_LINKS).text
            assert verify_link == self.IPAD_EXPECTED_NAMES[i], 'Text not expected'
            if verify_link == self.IPAD_EXPECTED_NAMES[-1]:
                print('Success!!!')

    def verify_number_links(self):
        links = self.driver.find_elements(*self.IPHONE_CLICKABLE_LINKS)
        print(links)
        assert len(links) == 4, f'expected 4 links but instead got {len(links)}'
