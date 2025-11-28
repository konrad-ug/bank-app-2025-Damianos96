import requests
import pytest

class TestApiCrud:
    url = "http://127.0.0.1:5000/api/accounts"

    @pytest.fixture
    def account_data(self):
        return {
            "name": "James",
            "surname": "Hetfield",
            "pesel": "89092909825"
        }

    @pytest.fixture
    def created_account(self, account_data):
        requests.post(self.url, json=account_data)
        yield account_data
        requests.delete(f"{self.url}/{account_data['pesel']}")

    def test_create_account(self, account_data):
        response = requests.post(self.url, json=account_data)
        assert response.status_code == 201
        assert response.json()["message"] == "Account created"

    def test_count(self):
        response = requests.get(f"{self.url}/count")
        assert response.status_code == 200
        assert response.json()["count"] == 1
    
    def test_get_account_by_pesel(self, created_account):
        pesel = created_account['pesel']
        name = created_account['name']
        surname = created_account['surname']
        response = requests.get(f"{self.url}/{pesel}")
        assert response.status_code == 200
        assert response.json()['name'] == name
        assert response.json()['surname'] == surname
        assert response.json()['pesel'] == pesel

    def test_get_account_not_found(self):
        response = requests.get(f"{self.url}/11111111111")
        assert response.status_code == 404
        assert response.json()["message"] == "Account not found"
    
    def test_update_account(self, created_account):
        pesel = created_account['pesel']
        update_data = {"surname": "Duda"}
        response = requests.patch(f"{self.url}/{pesel}", json=update_data)
        assert response.status_code == 200
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["surname"] == "Duda"
        assert check.json()["name"] == created_account["name"]

    def test_delete_account(self, created_account):
        pesel = created_account['pesel']
        response = requests.delete(f"{self.url}/{pesel}")
        assert response.status_code == 200
        assert response.json()["message"] == "Account deleted"
        check = requests.get(f"{self.url}/{pesel}")
        assert check.status_code == 404