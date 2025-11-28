import requests


class TestApi:
    def test_create_account(self):
        url = "http://127.0.0.1:5000/api/accounts"
        data = {
            "name": "james",
            "surname": "hetfield",
            "pesel": "89092909825"
        }
        response = requests.post(url, json=data)
        assert response.status_code == 201
        assert response.json() == {"message": "Account created"}