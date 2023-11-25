import requests
import allure

class BoardApi:
    
    @allure.step("URL: {base_url}, auth token {token}")
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token
    
    @allure.step("API. Get all boards for organization {org_id} ")
    def get_all_boards_by_org_id(self, org_id: str) -> list:
        
        path = "{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards/".format(trello = self.base_url, id = org_id)
        print(path)
        cookie = {"token": self.token}
        resp = requests.get(path, cookies=cookie)
        return resp.json().get("boards")
    
    @allure.step("API. Create new board {name}")
    def create_board(self, name: str, defaultLists=False) -> dict:
        
        body = {
            "defaultLists": defaultLists,
            "name": name,
            "token": self.token
        }
        cookie = {"token": self.token}
        path = "{trello}/boards/".format(trello=self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Delete board with id {id}")
    def delete_board_by_id(self, id: str) -> dict:
        body = {
            "token": self.token
        }
        
        cookie = {"token": self.token}
        path = "{trello}/boards/{board_id}".format(trello=self.base_url, board_id=id)
        resp = requests.delete(path, json=body, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Create list {name} in board {board_id}")
    def create_list(self, name: str, board_id: str) -> dict:
        body = {
            "token": self.token,
            "name": name,
            "idBoard": board_id 
        }
        cookie = {"token": self.token}
        path = "{trello}/boards/{board_id}/lists".format(trello=self.base_url, board_id=board_id)
        resp = requests.post(path, json=body, cookies=cookie)
        return resp.json()      

    @allure.step("API. Create card {name} in list {list_id}")
    def create_card(self, name: str, list_id: str) -> str:
        body = {
            "token": self.token,
            "idList": list_id,
            "name": name
        }
        cookie = {"token": self.token}
        path = "{trello}/cards".format(trello=self.base_url)
        resp = requests.post(path, json=body, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Update card {card_id} - new name is {new_name}")
    def update_card(self, new_name: str, card_id: str) -> dict:
        body = {
            "name": new_name,
            "token": self.token
        }
        cookie = {"token": self.token}
        path = "{trello}/cards/{card_id}".format(trello=self.base_url, card_id=card_id)
        resp = requests.put(path, json=body, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Move card {card_id} to another list {list_id}")
    def move_card(self, list_id: str, card_id: str):
        body = {
            "token": self.token,
            "idList": list_id
        }
        cookie = {"token": self.token}
        path = "{trello}/cards/{card_id}".format(trello=self.base_url, card_id=card_id)
        resp = requests.put(path, json=body, cookies=cookie)
        return resp.json()
    @allure.step("API. Get lists in board {board_id}")
    def get_lists_by_board_id(self, board_id: str) -> dict:
        path = "{trello}/boards/{board_id}/lists".format(trello=self.base_url, board_id=board_id)
        cookie = {"token": self.token}
        resp = requests.get(path, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Get card on list {list_id}")
    def get_card_on_list(self, list_id: str) -> dict:
        cookie = {"token": self.token}
        path = "{trello}/lists/{list_id}?fields=name".format(trello=self.base_url, list_id=list_id)
        resp = requests.get(path, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Get card {card_id}")
    def get_card_by_id(self, card_id: str):
        cookie = {"token": self.token}
        path = "{trello}/cards/{card_id}?fields=idlist,name,labels".format(trello=self.base_url, card_id=card_id)
        resp = requests.get(path, cookies=cookie)
        return resp.json()
    
    @allure.step("API. Delete card {card_id}")
    def delete_card(self, card_id: str, org_id: str) -> None:
        body = {
            "token": self.token  
        }
        cookie = {"token": self.token, "dsc": org_id}
        path = "{trello}/cards/{card_id}".format(trello=self.base_url, card_id=card_id)
        resp = requests.delete(path, json=body, cookies=cookie)
    
    @allure.step("API. Get all cards in list {list_id}")
    def get_cards_in_list(self, list_id: str):
        cookie = {"token": self.token}
        path = "{trello}/lists/{list_id}/cards".format(trello=self.base_url, list_id=list_id)
        resp = requests.get(path, cookies=cookie)
        return resp.json()