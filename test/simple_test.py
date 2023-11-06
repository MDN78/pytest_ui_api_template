from pages.AuthPage import AuthPage
import time


def test_auth(driver):
    auth_page = AuthPage(driver)
    auth_page.go()
    auth_page.login_as("salesakk@gmail.com", "")
    time.sleep(5)
    assert auth_page.get_current_url().endswith("mdn782007/boards")