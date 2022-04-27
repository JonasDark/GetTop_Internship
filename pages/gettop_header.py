from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class GettopHeader(Page):
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a[href*='product-category/iphone/']")
    # PRODUCT_CATEGORY = (By.CSS_SELECTOR, "a[href*='product-category/ipad/']")
    EXPECTED_NAMES = ['iPhone 12', 'iPhone 11', 'iPhone 11 Pro', 'iPhone SE']
    # EXPECTED_NAMES = ['iPad', 'iPad Pro', 'iPad mini', 'iPad Air']
    CURRENT_PAGE = (By.CSS_SELECTOR, 'h1.product-title')
    CLICKABLE_LINKS = (By.CSS_SELECTOR, "li#menu-item-469 ul.sub-menu li")
    # CLICKABLE_LINKS = (By.CSS_SELECTOR, "li#menu-item-470 ul.sub-menu li")

    def open_gettop_main(self):
        self.open_page()

    def hover_product_category(self):
        tab = self.find_element(*self.PRODUCT_CATEGORY)
        actions = ActionChains(self.driver)
        actions.move_to_element(tab)
        actions.perform()

    def verify_number_links(self):
        links = self.driver.find_elements(*self.CLICKABLE_LINKS)
        print(links)
        assert len(links) == 4, f'expected 4 links but instead got {len(links)}'

    def click_and_verify(self):
        click_link = self.driver.find_elements(*self.CLICKABLE_LINKS)
        for i in range(len(click_link)):
            self.hover_product_category()
            click_link = self.driver.find_elements(*self.CLICKABLE_LINKS)
            click_link[i].click()
            current_page = self.driver.find_element(*self.CURRENT_PAGE).text
            assert current_page == self.EXPECTED_NAMES[i], 'Text not expected'
            if current_page == self.EXPECTED_NAMES[-1]:
                print('Success!!!')
