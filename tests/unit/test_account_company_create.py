import pytest
from unittest.mock import patch
from src.company_account import CompanyAccount

class TestCompanyAccount:
    
    @patch('src.company_account.requests.get')
    def test_valid_account_creation(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Czynny"
                }
            }
        }
        
        company_account = CompanyAccount("Microsoft", "1234567890")
        assert company_account.company_name == "Microsoft"
        assert company_account.nip == "1234567890"
        assert company_account.balance == 0.0
        mock_get.assert_called_once()
    
    @patch('src.company_account.requests.get')
    def test_account_creation_failed_not_registered(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "result": {
                "subject": {
                    "statusVat": "Zwolniony"
                }
            }
        }
        with pytest.raises(ValueError, match="Company not registered!!"):
            CompanyAccount("Microsoft", "1234567890")

    @patch('src.company_account.requests.get')
    def test_nip_too_long(self, mock_get):
        company_account = CompanyAccount("Microsoft", "1234567890123")
        assert company_account.nip == "1234567890123" 
        mock_get.assert_not_called()

    @patch('src.company_account.requests.get')
    def test_nip_too_short(self, mock_get):
        company_account = CompanyAccount("Microsoft", "123")
        assert company_account.nip == "123"
        mock_get.assert_not_called()