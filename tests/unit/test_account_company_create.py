from src.company_account import CompanyAccount

class TestCompanyAccount:
    def test_valid_account_creation(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        assert company_account.company_name == "Microsoft"
        assert company_account.nip == "1231231231"
        assert company_account.balance == 0.0
    
    def test_nip_too_long(self):
        company_account = CompanyAccount("Microsoft", "32231231231231")
        assert company_account.nip == "Invalid"

    def test_nip_too_short(self):
        company_account = CompanyAccount("Microsoft", "3231231")
        assert company_account.nip == "Invalid"
    
    def test_nip_none(self):
        company_account = CompanyAccount("Microsoft", None)
        assert company_account.nip == "Invalid"

