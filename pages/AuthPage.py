from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from configuration.ConfigProvider import ConfigProvider
from testdata.DataProvider import DataProvider

class AuthPage:

    def __init__(self, driver: WebDriver) ->None:
        url = ConfigProvider().get("ui", "base_url")
        self.url = f"{url}/login"
        self.__driver = driver
    
    @allure.step("UI. Go to authorization page")
    def go(self) -> None:
        self.__driver.get(self.url)
    
    @allure.step("UI. Authorization with login {email}")  
    def login_as(self, email: str, password: str):
        self.__driver.find_element(By.CSS_SELECTOR, "#user").send_keys(email)
        self.__driver.find_element(By.CSS_SELECTOR, "#login").click()
        # дожидаемся отрисовки поля Пароль
        WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "svg[role='presentation']")))
        self.__driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.__driver.find_element(By.CSS_SELECTOR, "#login-submit").click()
    
    @allure.step("UI. Get current url")
    def get_current_url(self):
        return self.__driver.current_url
    
