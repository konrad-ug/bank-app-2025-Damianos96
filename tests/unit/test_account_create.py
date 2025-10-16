from src.account import Account

class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "12345678912")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0

    def test_pesel_too_long(self):
        account = Account("Jane", "Smith", "198421941984149")
        assert account.pesel == "Invalid"
    
    def test_pesel_too_short(self):
        account = Account("Jane", "Smith", "21313")
        assert account.pesel == "Invalid"
    
    def test_pesel_empty(self):
        account = Account("Jane", "Smith", "")
        assert account.pesel == "Invalid"

    def test_valid_promo_code(self):
        account = Account("Jane", "Smith", "04295678910", "PROM_ABC")
        assert account.balance == 50.0
    
    def test_invalid_code_prefix(self):
        account = Account("Jane", "Smith", "12345678910", "PRxM_ab1")
        assert account.balance == 0.0
    
    def test_invalid_code_suffix(self):
        account = Account("Jane", "Smith", "12345678910", "PRxM_ab1")
        assert account.balance == 0.0
    
    def test_valid_code_age(self):
        account = Account("Jane", "Smith", "04295678910", "PROM_ab1")
        assert account.balance == 50.0
    
    def test_invalid_code_age(self):
        account = Account("Jane", "Smith", "12105678910", "PROM_ab1")
        assert account.balance == 0.0
        
    