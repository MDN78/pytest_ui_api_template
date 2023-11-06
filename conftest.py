import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    
    driver.quit()