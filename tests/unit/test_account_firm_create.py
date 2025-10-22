from src.firm_account import FirmAccount

class TestFirmAccount:
    def test_valid_account_creation(self):
        firm_account = FirmAccount("Microsoft", "1231231231")
        assert firm_account.company_name == "Microsoft"
        assert firm_account.nip == "1231231231"
        assert firm_account.balance == 0.0
    
    def test_nip_too_long(self):
        firm_account = FirmAccount("Microsoft", "32231231231231")
        assert firm_account.nip == "Invalid"

    def test_nip_too_short(self):
        firm_account = FirmAccount("Microsoft", "3231231")
        assert firm_account.nip == "Invalid"
    
    def test_nip_none(self):
        firm_account = FirmAccount("Microsoft", None)
        assert firm_account.nip == "Invalid"

