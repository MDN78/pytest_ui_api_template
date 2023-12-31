from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testdata.DataProvider import DataProvider
from configuration.ConfigProvider import ConfigProvider
from selenium.webdriver import ActionChains
from selenium import webdriver
import allure



class MainPage:
    
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.data = DataProvider()
    
    @allure.step("Get current url")  
    def get_current_url(self) -> str:
        
        return self.__driver.current_url
    
    @allure.step("UI. Open right side menu")
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid='header-member-menu-button']").click()
    
    @allure.step("UI. Get information about user")
    def get_account_info(self) -> list[str]:
        container = self.__driver.find_element(By.CSS_SELECTOR, "div[class=mJBO4dHZbrIG_0]")
        fields = container.find_elements(By.CSS_SELECTOR, "div")
        name = fields[0].text
        email = fields[1].text
        return [name, email]

    @allure.step("UI. Open create form")
    def open_create_form(self):
        self.__driver.find_element(By.CSS_SELECTOR, "button[data-testid=header-create-menu-button]").click()
    
    @allure.step("UI. Choose {number} element in list")
    def press_button_create_board(self, number=1):
        pop = self.__driver.find_element(By.CSS_SELECTOR, "section[data-testid=header-create-menu-popover]")
        menu_list = pop.find_elements(By.CSS_SELECTOR, "li")
        menu_list[number-1].click()
    
    @allure.step("UI.Select board {number} in workspace")
    def select_board(self, number=0):
        pop = self.__driver.find_element(By.CSS_SELECTOR, "ul[class=boards-page-board-section-list]")
        menu_list = pop.find_elements(By.CSS_SELECTOR, "li")
        menu_list[number].click()
    
    @allure.step("UI. Delete board")
    def delete_board(self):
        self.__driver.find_element(By.XPATH, "//div[@class='board-header u-clearfix js-board-header']//div//span[2]//button[2]//span//span").click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.board-menu-navigation-item-link.board-menu-navigation-item-link-v2.js-close-board"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.js-confirm.full.nch-button.nch-button--danger"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid=close-board-delete-board-button]"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='close-board-delete-board-confirm-button']"))).click()
  


    @allure.step("UI. Set board name {board_name}")
    def fill_board_name(self, board_name: str):
        self.__driver.find_element(By.CSS_SELECTOR, "input[data-testid=create-board-title-input]").send_keys(board_name)
    
    @allure.step("UI. Press button 'Create' via")
    def click_create_button(self):
        button = WebDriverWait(self.__driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid=create-board-submit-button]")))
        button.click()
        WebDriverWait(self.__driver, 20).until(EC.url_contains("https://trello.com/b/"))
        
    @allure.step("UI. Crerate new list {list_name}")
    def create_list(self, list_name: str) -> str:
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='list-composer-button']"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-testid=list-name-textarea]"))).send_keys(list_name)
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='list-composer-add-list-button']"))).click()
        list_name = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h2[data-testid='list-name']")))
        return list_name.text
        
    @allure.step("UI. Create new card {card_name}")
    def create_card(self, card_name: str) -> str:
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid=list-add-card-button]"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea[data-testid=list-card-composer-textarea]"))).send_keys(card_name)
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid=list-card-composer-add-card-button]"))).click()
        card_name = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid=card-name]")))
        return card_name.text
        
        
    @allure.step("UI. Drag and drop card to another list")
    def drag_and_drop_onto_element(self) -> str:
        draggable = self.__driver.find_element(By.CSS_SELECTOR, "div[data-testid=trello-card]")
        droppable = self.__driver.find_element(By.CSS_SELECTOR, "ol[data-testid=list-cards]")
        ActionChains(self.__driver)\
            .drag_and_drop(draggable, droppable)\
            .perform()
        new_name = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.NdQKKfeqJDDdX3")))
        return new_name.text
    
    @allure.step("UI. Update title card - new name {new_card_name}")
    def update_card(self, new_card_name: str) -> str:
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid=card-name]"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.mod-card-back-title.js-card-detail-title-input"))).clear()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.mod-card-back-title.js-card-detail-title-input"))).send_keys(new_card_name)
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.icon-md.icon-close.dialog-close-button.js-close-window"))).click()
        new_name = WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid=card-name]")))
        return new_name.text
    
    @allure.step("UI. Delete card")
    def delete_card(self):
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid=card-name]"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button-link.js-archive-card"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button-link.js-delete-card.negate"))).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.js-confirm.full.nch-button.nch-button--danger"))).click()