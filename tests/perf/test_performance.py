import requests
import pytest
import time

class TestPerformance:
    BASE_URL = "http://127.0.0.1:5000/api/accounts"

    def test_perf_create_and_delete_account(self):
        for i in range(100):
            pesel = f"99{i:09d}" 
            payload = {
                "name": "Perf",
                "surname": "Test",
                "pesel": pesel
            }

            start_time = time.time()
            response_create = requests.post(self.BASE_URL, json=payload, timeout=0.5)
            end_time = time.time()
            
            assert response_create.status_code == 201
            assert end_time - start_time < 0.5, f"Create account took too long: {end_time - start_time}"

            start_time = time.time()
            response_delete = requests.delete(f"{self.BASE_URL}/{pesel}", timeout=0.5)
            end_time = time.time()

            assert response_delete.status_code == 200
            assert end_time - start_time < 0.5, f"Delete account took too long: {end_time - start_time}"

    def test_perf_transfers(self):
        pesel = "88888888888"
        payload = {
            "name": "Transfer",
            "surname": "Master",
            "pesel": pesel
        }

        requests.post(self.BASE_URL, json=payload)

        try:
            for _ in range(100):
                transfer_data = {"type": "incoming", "amount": 1}
                
                start_time = time.time()
                response = requests.post(
                    f"{self.BASE_URL}/{pesel}/transfer", 
                    json=transfer_data, 
                    timeout=0.5
                )
                end_time = time.time()

                assert response.status_code == 200
                assert end_time - start_time < 0.5, f"Transfer took too long: {end_time - start_time}"

            response_get = requests.get(f"{self.BASE_URL}/{pesel}")
            assert response_get.status_code == 200
            assert response_get.json()["balance"] == 100

        finally:
            requests.delete(f"{self.BASE_URL}/{pesel}")

    def test_perf_bulk_create_and_delete(self):
        created_pesels = []

        for i in range(1000):
            pesel = f"77{i:09d}"
            created_pesels.append(pesel)
            payload = {"name": "Bulk", "surname": "Test", "pesel": pesel}
            
            resp = requests.post(self.BASE_URL, json=payload, timeout=0.5)
            assert resp.status_code == 201

        resp_count = requests.get(f"{self.BASE_URL}/count")

        assert resp_count.elapsed.total_seconds() < 0.5

        for pesel in created_pesels:
            resp = requests.delete(f"{self.BASE_URL}/{pesel}", timeout=0.5)
            assert resp.status_code == 200