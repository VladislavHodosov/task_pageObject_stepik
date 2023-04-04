from .base_page import BasePage
from .locators import ProductsLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductsLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_alert_product_name(self):
        element = self.wait_for_element_present(*ProductsLocators.ALERT_SUCCESS)
        return element.text

    def get_alert_basket_price(self):
        element = self.wait_for_element_present(*ProductsLocators.ALERT_INFO_LABEL)
        return element.text

    def get_product_price(self):
        element = self.browser.find_element(*ProductsLocators.PRODUCT_PRICE_LABEL)
        return element.text

    def get_product_name(self):
        element = self.browser.find_element(*ProductsLocators.PRODUCT_NAME_LABEL)
        return element.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductsLocators.ALERT_SUCCESS), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductsLocators.ALERT_SUCCESS), \
            "Success message is presented, but should not be"