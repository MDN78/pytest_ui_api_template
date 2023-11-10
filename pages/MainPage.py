from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata.DataProvider import DataProvider
import allure



class MainPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()
    
    @allure.step("Get current url")  
    def get_current_url(self) -> str:
        return self.__driver.current_url
    
    @allure.step("Open right side menu")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-member-menu-button']").click()
    
    @allure.step("Get information about user")
    def get_account_info(self) -> list[str]:
        container = self.__driver.find_element(By.CSS_SELECTOR, "div[class=mJBO4dHZbrIG_0]")
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        name = fields[0].text
        email = fields[1].text
        
        return [name, email]
    
    @allure.step("Add auth cookie")
    def add_cookie(self):
        cookie = {
            "name": "token",
            "value": self.data.get_token()
        }


    