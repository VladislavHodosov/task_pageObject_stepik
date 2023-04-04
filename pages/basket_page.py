from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_ITEMS), \
            "There are items in basket"

    def empty_label_is_present(self):
        assert self.is_element_present(*BasketLocators.BASKET_IS_EMPTY_LABEL), \
            "There is no empty label"