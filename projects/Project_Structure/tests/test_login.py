import allure
from pages.login_page import LoginPage

@allure.feature("Login Test")
def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # assert login_page.is_login_successful()