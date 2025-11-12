from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
import pytest

class TestTransfersPersonal:
    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678901")
        return account
    
    def test_test_express_transfer_equal(self, account):
        account.balance=100.0
        account.express_transfer(100.0)
        assert account.balance == -1.00
    
    def test_test_express_insufficient_balance(self, account):
        account.balance=100.0
        account.express_transfer(200.0)
        assert account.balance == 100.0
    
    def test_test_express_sufficient_balance(self, account):
        account.balance=100.0
        account.express_transfer(50.0)
        assert account.balance == 49.0

    def test_test_express_transfer_negative(self, account):
        account.balance=100.0
        account.express_transfer(-50.0)
        assert account.balance == 100.0
    
    def test_express_transfer_zero(self, account):
        account.balance = 100.0
        account.express_transfer(0.0)
        assert account.balance == 100.0

class TestTransfersCompany:
    @pytest.fixture
    def company_account(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        return company_account
    
    def test_test_express_transfer_equal(self, company_account):
        company_account.balance = 100.0
        company_account.express_transfer(100.0)
        assert company_account.balance == -5.0

    def test_test_express_insufficient_balance(self, company_account):
        company_account.balance = 100.0
        company_account.express_transfer(200.0)
        assert company_account.balance == 100.0
    
    def test_test_express_sufficient_balance(self, company_account):
        company_account.balance = 100.0
        company_account.express_transfer(50.0)
        assert company_account.balance == 45.0

    def test_test_express_transfer_negative(self, company_account):
        company_account.balance = 100.0
        company_account.express_transfer(-50.0)
        assert company_account.balance == 100.0
    
    def test_express_transfer_zero(self, company_account):
        company_account.balance = 100.0
        company_account.express_transfer(0.0)
        assert company_account.balance == 100.0