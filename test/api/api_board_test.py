from api.BoardApi import BoardApi
import pytest

@pytest.mark.skip
def test_get_boards(api_client: BoardApi, testdata: dict):
    org_id = testdata.get("org_id")
    board_list = api_client.get_all_boards_by_org_id(org_id)
    count = len(board_list)
    print(count)
    print(board_list)
    assert count == 1

@pytest.mark.skip
def test_create_board(api_client: BoardApi, delete_board: dict, testdata: dict):
    org_id = testdata.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.create_board("New board to be deleted")
    
    delete_board["board_id"] = resp.get("id")
    
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    print(resp)
    
    assert len(board_list_after) - len(board_list_before) == 1

@pytest.mark.skip
def test_delete_board(api_client: BoardApi, dummy_board_id: str, testdata: dict):
    org_id = testdata.get("org_id")
    board_list_before = api_client.get_all_boards_by_org_id(org_id)
    resp = api_client.delete_board_by_id(dummy_board_id)
    board_list_after = api_client.get_all_boards_by_org_id(org_id)
    
    assert len(board_list_after) == 1
    
    
    

