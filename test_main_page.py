from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
# def test_that_add_basket_button_present(browser):
#     browser.get(link)
#     WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class*='add-to-basket']")))
#     buttonAddToBasket = browser.find_element(By.CSS_SELECTOR, "button[class*='add-to-basket']")
#     assert buttonAddToBasket.is_displayed() is True