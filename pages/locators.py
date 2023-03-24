from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    EMAIL_TEXTBOX = (By.ID, "id_login-username")
    PASS_TEXTBOX = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")