from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
import time
import allure

def test_auth(driver):
    email = "salesakk@gmail.com"
    password = ""
    username = "Dimitri"
    auth_page = AuthPage(driver)
    auth_page.go()
    auth_page.login_as(email, password)
    time.sleep(5)
    
    main_page = MainPage(driver)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    with allure.step("Checking the right link"):
        assert main_page.get_current_url().endswith("mdn782007/boards")
    with allure.step("Checking user info"):
        assert info[0] == username
        assert info[1] == email