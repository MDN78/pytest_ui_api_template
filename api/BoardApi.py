import requests

class BoardApi:
    
    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token
    
    def get_all_boards_by_org_id(self, org_id: str) -> list:
        
        path = "{trello}/organizations/{id}?boards=open&board_fields=all&fields=boards/".format(trello = self.base_url, id = org_id)
        print(path)
        cookie = {"token": self.token}
        
        resp = requests.get(path, cookies=cookie)
        
        return resp.json().get("boards")
    
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
    
    def delete_board_by_id(self, id: str):
        body = {
            "token": self.token
        }
        
        cookie = {"token": self.token}
        path = "{trello}/boards/{board_id}".format(trello=self.base_url, board_id=id)
        resp = requests.delete(path, json=body, cookies=cookie)
        return resp.json()