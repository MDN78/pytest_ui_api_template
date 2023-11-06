from pages import AuthPage
from selenium import webdriver

def test_first():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    
    auth_page = AuthPage()
    
    a = 101