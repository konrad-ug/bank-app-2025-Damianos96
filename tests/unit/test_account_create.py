from src.account import Account

class TestAccount:
    def test_account_creation(self):
        account = Account("John", "Doe", "123456789112")
        assert account.first_name == "John"
        assert account.last_name == "Doe"
        assert account.balance == 0.0
        # if len(promo_code) == 0:
        #     assert promo_code == None
        # else if promo_code[0:5] != "PROM_":
        #     assert promo_code == "Invalid"
        # else:
        #     assert promo_code[0:5] == "PROM_" and len(promo_code) > 8

    def test_pesel_too_long(self):
        account = Account("Jane", "Smith", "198421941984149")
        assert account.pesel == "Invalid"
    
    def test_pesel_too_short(self):
        account = Account("Jane", "Smith", "21313")
        assert account.pesel == "Invalid"
    
    def test_pesel_empty(self):
        account = Account("Jane", "Smith", "")
        assert account.pesel == "Invalid"

    def test_promo_code_format(self):
        account = Account("Jane", "Smith", "12345678910", "PRom_ABCDEF")
        assert account.promo_code == "Invalid"

    def test_promo_code_length(self):
        account = Account("Jane", "Smith", "12345678910", "PROM_AB")
        assert account.promo_code == "Invalid"
    
    def test_promo_code_valid(self):
        account = Account("Jane", "Smith", "12345678910", "PROM_ABCDEF")
        assert account.promo_code == "PROM_ABCDEF"

    