from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
import time


def test_auth(driver):
    auth_page = AuthPage(driver)
    auth_page.go()
    auth_page.login_as("salesakk@gmail.com", "")
    time.sleep(5)
    
    main_page = MainPage(driver)
    main_page.open_menu()
    info = main_page.get_account_info()
    
    assert main_page.get_current_url().endswith("mdn782007/boards")
    assert info[0] == "Dimitri"
    assert info[1] == "salesakk@gmail.com"