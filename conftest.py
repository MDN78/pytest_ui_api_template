import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import allure


@pytest.fixture
def driver():
    with allure.step("Open and prepare browser"):
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        driver.maximize_window()
        yield driver
    
    with allure.step("Close browser"):
        driver.quit()