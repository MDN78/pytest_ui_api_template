from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthPage:
    
    def __init__(self, driver: WebDriver) ->None:
        self.url = "https://trello.com/login?returnUrl=%2Fu%2Fmdn782007%2Fboards"
        self.__driver = driver
    
    def go(self):
        self.__driver.get(self.url)