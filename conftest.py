import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import allure
from api.BoardApi import BoardApi
from configuration.ConfigProvider import ConfigProvider

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from testdata.DataProvider import DataProvider



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
    token = DataProvider().get_token()
    return BoardApi(url, token)

@pytest.fixture
def api_client_no_auth() -> BoardApi:
    url = ConfigProvider().get("api", "base_url")
    token = DataProvider().get_token()
    return BoardApi(url, token)

@pytest.fixture
def dummy_board_id() -> str:
    url = ConfigProvider().get("api", "base_url")
    token = DataProvider().get_token()
    api = BoardApi(url, token)
    resp = api.create_board("Board to be deleted").get("id")
    return resp

@pytest.fixture
def delete_board() -> str:
    dictionary = {"board_id": ""}
    yield dictionary
    url = ConfigProvider().get("api", "base_url")
    token = DataProvider().get_token()
    api = BoardApi(url, token)
    api.delete_board_by_id(dictionary.get("board_id"))
    
@pytest.fixture
def testdata() -> dict:
    return DataProvider()