import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager




@pytest.fixture
def driver():
    with allure.step("Open and prepare browser"):
        timeout = ConfigProvider().getint("ui", "timeout")
        
        driver_name = ConfigProvider().get("ui", "browser_name")
        driver = None
        
        if driver_name == 'chrome':
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        
        driver.implicitly_wait(timeout)
        driver.maximize_window()
        yield driver
    
    with allure.step("Close browser"):
        driver.quit()
        
@pytest.fixture
def api_client() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, "        ")

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    return BoardApi(url, "")

@pytest.fixture
def dummy_board_id() -> str:
    url = ConfigProvider().get("api", "base_url")
    api = BoardApi(url, "     ")
    resp = api.create_board("Board to be deleted").get("id")
    return resp

@pytest.fixture
def delete_board() -> str:
    url = ConfigProvider().get("api", "base_url")
    dictionary = {"board_id": ""}
    yield dictionary
    api = BoardApi(url, "    ")
    api.delete_board_by_id(dictionary.get("board_id"))