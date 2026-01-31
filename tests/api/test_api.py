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

    def test_create_account_valid_and_with_pesel_in_use(self, account_data):
        response = requests.post(self.url, json=account_data)
        response2 = requests.post(self.url, json=account_data)
        assert response.status_code == 201
        assert response.json()["message"] == "Account created"
        assert response2.status_code == 409
        assert response2.json()["message"] == "Account with this pesel already exists"

    def test_count(self):
        response = requests.get(f"{self.url}/count")
        assert response.status_code == 200
        assert response.json()["count"] == 2
    
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
    
    def test_incoming_transfer(self, created_account):
        pesel = created_account['pesel']
        payload = {"amount": 100, "type": "incoming"}
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 200
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["balance"] == 100

    def test_outgoing_transfer_success(self, created_account):
        pesel = created_account['pesel']
        requests.post(f"{self.url}/{pesel}/transfer", json={"amount": 200, "type": "incoming"})
        payload = {"amount": 100, "type": "outgoing"}
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 200
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["balance"] == 100

    def test_outgoing_transfer_fail(self, created_account):
        pesel = created_account['pesel']
        payload = {"amount": 100, "type": "outgoing"}
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 422
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["balance"] == 0

    def test_transfer_unknown_type(self, created_account):
        pesel = created_account['pesel']
        payload = {"amount": 100, "type": "crypto"}        
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 400

    def test_express_transfer(self, created_account):
        pesel = created_account['pesel']
        requests.post(f"{self.url}/{pesel}/transfer", json={"amount": 100, "type": "incoming"})
        payload = {"amount": 50, "type": "express"}
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 200
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["balance"] == 49

    def test_express_transfer_insufficient_funds_for_fee_equal_balance(self, created_account):
        pesel = created_account['pesel']
        requests.post(f"{self.url}/{pesel}/transfer", json={"amount": 100, "type": "incoming"})
        payload = {"amount": 100, "type": "express"}
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 200
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["balance"] == -1.0

    def test_express_transfer_insufficient_funds_for_fee(self, created_account):
        pesel = created_account['pesel']
        requests.post(f"{self.url}/{pesel}/transfer", json={"amount": 100, "type": "incoming"})
        payload = {"amount": 200, "type": "express"}
        response = requests.post(f"{self.url}/{pesel}/transfer", json=payload)
        assert response.status_code == 422
        check = requests.get(f"{self.url}/{pesel}")
        assert check.json()["balance"] == 100

    def test_transfer_account_not_found(self):
        payload = {"amount": 100, "type": "incoming"}
        response = requests.post(f"{self.url}/00000000000/transfer", json=payload)
        assert response.status_code == 404