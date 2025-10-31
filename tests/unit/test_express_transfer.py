from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestTransfersPersonal:
    def test_test_express_transfer_equal(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance=100.0
        personal_account.express_transfer(100.0)
        assert personal_account.balance == -1.00
    
    def test_test_express_insufficient_balance(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance=100.0
        personal_account.express_transfer(200.0)
        assert personal_account.balance == 100.0
    
    def test_test_express_sufficient_balance(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance=100.0
        personal_account.express_transfer(50.0)
        assert personal_account.balance == 49.0

    def test_test_express_transfer_negative(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance=100.0
        personal_account.express_transfer(-50.0)
        assert personal_account.balance == 100.0
    
    def test_express_transfer_zero(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.express_transfer(0.0)
        assert personal_account.balance == 100.0

class TestTransfersCompany:
    def test_test_express_transfer_equal(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.express_transfer(100.0)
        assert company_account.balance == -5.0

    def test_test_express_insufficient_balance(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.express_transfer(200.0)
        assert company_account.balance == 100.0
    
    def test_test_express_sufficient_balance(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.express_transfer(50.0)
        assert company_account.balance == 45.0

    def test_test_express_transfer_negative(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.express_transfer(-50.0)
        assert company_account.balance == 100.0
    
    def test_express_transfer_zero(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.express_transfer(0.0)
        assert company_account.balance == 100.0