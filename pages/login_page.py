from .locators import LoginPageLocators
from .base_page import BasePage

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        self.wait_for_element_present(*LoginPageLocators.REGISTER_FORM)
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_TEXTBOX)
        pas = self.browser.find_element(*LoginPageLocators.PASS_REGISTER_TEXTBOX)
        conf_pas = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_TEXTBOX)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_field.send_keys(email)
        pas.send_keys(password)
        conf_pas.send_keys(password)
        register.click()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url isn't correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"