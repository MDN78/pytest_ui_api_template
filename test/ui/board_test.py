from pages.AuthPage import AuthPage
from pages.MainPage import MainPage
from api.BoardApi import BoardApi
import time
import allure
import pytest

@pytest.mark.skip
def test_create_board(driver, api_client: BoardApi, testdata: dict):
    email = testdata.get("email")
    password = testdata.get("password")
    auth_page = AuthPage(driver)
    auth_page.go()
    auth_page.login_as(email, password)
    main_page = MainPage(driver)
    main_page.open_create_form()
    main_page.press_button_create_board()
    main_page.fill_board_name("New board UI")
    main_page.click_create_button()
    
    time.sleep(3)
    current_url = main_page.get_current_url()
    with allure.step(f"Checking that {current_url} ends on /new-board-ui"):
        assert current_url.endswith("/new-board-ui")
    
    org_id = testdata.get("org_id")
    info = api_client.get_all_boards_by_org_id(org_id)
    board_name = info[0]["name"]
    board_id = info[0]["id"]
    assert board_name == "New board UI"
    api_client.delete_board_by_id(board_id)

@pytest.mark.skip
def test_delete_board(driver_auth):
    main_page = MainPage(driver_auth)
    main_page.open_create_form()
    main_page.press_button_create_board()
    main_page.fill_board_name("New board for delete")
    main_page.click_create_button()
    
    # main_page.select_board()
    time.sleep(2)
    main_page.delete_board()
    time.sleep(2)
    current_url = main_page.get_current_url()
    with allure.step(f"Checking that {current_url} ends on /boards"):
        assert current_url.endswith("/boards")

@pytest.mark.skip
def test_create_list(driver_auth, dummy_board_id: str, api_client: BoardApi):
    time.sleep(3)
    main_page = MainPage(driver_auth)
    main_page.select_board()
    main_page.create_list("New list")
    time.sleep(3)
    api_client.delete_board_by_id(dummy_board_id)

@pytest.mark.skip
def test_create_card(driver_auth, dummy_list_id: list, api_client: BoardApi):
    main_page = MainPage(driver_auth)
    main_page.select_board()
    main_page.create_card("New card")
    time.sleep(3)
    api_client.delete_board_by_id(dummy_list_id[1])

@pytest.mark.skip 
def test_create_two_lists(driver_auth, dummy_two_lists_id: list):
    main_page = MainPage(driver_auth)
    main_page.select_board()
    time.sleep(4)

@pytest.mark.skip
def test_drag_and_drop(driver_auth, dummy_two_lists_id: list, api_client: BoardApi):
    main_page = MainPage(driver_auth)
    main_page.select_board()
    api_client.create_card("new card", dummy_two_lists_id[1])
    main_page.drag_and_drop_onto_element()
    time.sleep(3)
    api_client.delete_board_by_id(dummy_two_lists_id[0])
    
@pytest.mark.skip
def test_update_card(driver_auth, dummy_card_id: list, api_client: BoardApi):
    main_page = MainPage(driver_auth)
    main_page.select_board()
    name = main_page.update_card("Name for update")
    assert name == "Name for update"
    api_client.delete_board_by_id(dummy_card_id[0])

