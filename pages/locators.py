from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[text() = 'View basket']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    EMAIL_TEXTBOX = (By.ID, "id_login-username")
    PASS_TEXTBOX = (By.ID, "id_login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTER_TEXTBOX = (By.ID, "id_registration-email")
    PASS_REGISTER_TEXTBOX = (By.ID, "id_registration-password1")
    CONFIRM_REGISTER_TEXTBOX = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductsLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to')]")
    PRODUCT_PRICE_LABEL = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_LABEL = (By.XPATH, "//h1")
    ALERT_INFO_LABEL = (By.CSS_SELECTOR, "div.alert-info strong")
    ALERT_SUCCESS = (By.XPATH, "//div[contains(@class, 'alert-success')][1]//strong")

class BasketLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_LABEL = (By.CSS_SELECTOR, "#content_inner p")