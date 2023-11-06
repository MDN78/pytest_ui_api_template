from pages.AuthPage import AuthPage
import time


def test_auth(driver):
    auth_page = AuthPage(driver)
    auth_page.go()
    auth_page.login_as("salesakk@gmail.com", "insert email")
    time.sleep(5)