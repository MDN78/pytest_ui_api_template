from api.BoardApi import BoardApi
import allure
import pytest

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Create list")
def test_create_list(api_client: BoardApi, dummy_board_id: str, testdata: dict ):
    org_id = testdata.get("org_id")
    api_client.create_list("new list for test", dummy_board_id)
    board_lists = api_client.get_lists_by_board_id(dummy_board_id)
    assert len(board_lists) != 0
    api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after) == 0

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Edit card")
def test_edit_cart(api_client: BoardApi, dummy_card_id: str, testdata: dict):
    new_card = api_client.update_card("Foxtrot", dummy_card_id[1])
    assert new_card["name"] == "Foxtrot"
    api_client.delete_board_by_id(dummy_card_id[0])
    
    org_id = testdata.get("org_id")
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    assert len(board_list_after) == 0

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Move card to another list")
def test_move_cart(api_client: BoardApi, dummy_card_id: list):
    board_list_before = api_client.get_lists_by_board_id(dummy_card_id[0])
   
    additional_list = api_client.create_list("List for moving card", dummy_card_id[0]).get("id")
    move_card = api_client.move_card(additional_list, dummy_card_id[1])
    assert move_card["name"] != []

    board_lists_after = api_client.get_lists_by_board_id(dummy_card_id[0])
    assert len(board_lists_after) > len(board_list_before)
    
    api_client.delete_board_by_id(dummy_card_id[0])

@allure.epic("API tests")
@allure.severity(severity_level='normal')
@allure.title("Delete card")
def test_delete_card(api_client: BoardApi, dummy_card_id: list, testdata: dict):
    card_info_before = api_client.get_cards_in_list(dummy_card_id[2])
    assert card_info_before != []
    
    org_id = testdata.get("org_id")
    api_client.delete_card(dummy_card_id[1], org_id)
    card_info_after = api_client.get_cards_in_list(dummy_card_id[2])
    assert card_info_after == []
    
    api_client.delete_board_by_id(dummy_card_id[0])

