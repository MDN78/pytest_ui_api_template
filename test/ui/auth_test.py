from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
import time
import allure
import pytest

@allure.epic("UI tests")
@allure.severity(severity_level='normal')
@allure.title("Authorization")
def test_auth(driver, testdata: dict):
    email = testdata.get("email")
    password = testdata.get("password")
    username = testdata.get("username")
    auth_page = AuthPage(driver)
    auth_page.go()
    auth_page.login_as(email, password)
    time.sleep(5)
    
    main_page = MainPage(driver)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    current_url = main_page.get_current_url()
    with allure.step(f"Checking that {current_url} ends on /boards"):
        assert current_url.endswith("/boards")
    with allure.step("Checking user info"):
        assert info[0] == username
        assert info[1] == email

