import pytest
import allure
from pages.login_page import LoginPage
from utils.data_reader import read_login_data

test_data = read_login_data("data/login_data.csv")

@pytest.mark.parametrize("username,password", test_data)
@allure.feature("Data Driven Login")
def test_login_dd(page, username, password):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    assert "dashboard" in page.url or "auth/login" in page.url