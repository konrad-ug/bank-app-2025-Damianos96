import requests
import pytest
import time

class TestApiSaveLoad:
    BASE_URL = "http://127.0.0.1:5000/api/accounts"

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        yield
    
    def test_save_and_load_flow(self):
        pesel = "55555555555"
        payload = {"name": "Test", "surname": "Save", "pesel": pesel}
        requests.post(self.BASE_URL, json=payload)

        response_save = requests.post(f"{self.BASE_URL}/save")
        assert response_save.status_code == 200
        assert response_save.json()["message"] == "Accounts saved successfully"

        requests.post(self.BASE_URL, json={"name": "Ghost", "surname": "User", "pesel": "00000000000"})
        
        assert requests.get(f"{self.BASE_URL}/count").json()["count"] == 2

        response_load = requests.post(f"{self.BASE_URL}/load")
        assert response_load.status_code == 200
        
        assert requests.get(f"{self.BASE_URL}/count").json()["count"] == 1
        
        acc = requests.get(f"{self.BASE_URL}/{pesel}")
        assert acc.status_code == 200
        assert acc.json()["name"] == "Test"