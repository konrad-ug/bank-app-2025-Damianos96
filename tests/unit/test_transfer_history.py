from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
import pytest

class TestPersonalTransferHistory:
    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        return account
    
    def test_incoming_transfer_history(self, account):
        account.balance = 100.0
        account.incoming_transfer(50.0)
        assert account.history == [50.0]
    
    def test_double_incoming_transfer_history(self, account):
        account.balance = 100.0
        account.incoming_transfer(50.0)
        account.incoming_transfer(20.0)
        assert account.history == [50.0, 20.0]
    
    def test_outgoing_transfer_history(self, account):
        account.balance = 100.0
        account.outgoing_transfer(50.0)
        assert account.history == [-50.0]
    
    def test_double_outgoing_transfer_history(self, account):
        account.balance = 100.0
        account.outgoing_transfer(50.0)
        account.outgoing_transfer(20.0)
        assert account.history == [-50.0, -20.0]

    def test_mixed_transfer_history(self, account):
        account.balance = 100.0
        account.outgoing_transfer(50.0)
        account.incoming_transfer(20.0)
        assert account.history == [-50.0, 20.0]
    
    def test_express_transfer_history(self, account):
        account.balance = 100.0
        account.express_transfer(50.0)
        assert account.history == [-50.0, -1.0]
    
    def test_express_and_normal_transfer_history(self, account):
        account.balance = 100.0
        account.incoming_transfer(500.0)
        account.express_transfer(300.0)
        assert account.history == [500.0, -300.0, -1.0]

class TestCompanyTransferHistory:
    @pytest.fixture
    def company_account(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        return company_account
    
    def test_incoming_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.incoming_transfer(50.0)
        assert company_account.history == [50.0]
    
    def test_double_incoming_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.incoming_transfer(50.0)
        company_account.incoming_transfer(20.0)
        assert company_account.history == [50.0, 20.0]
    
    def test_outgoing_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.outgoing_transfer(50.0)
        assert company_account.history == [-50.0]
    
    def test_double_outgoing_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.outgoing_transfer(50.0)
        company_account.outgoing_transfer(20.0)
        assert company_account.history == [-50.0, -20.0]

    def test_mixed_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.outgoing_transfer(50.0)
        company_account.incoming_transfer(20.0)
        assert company_account.history == [-50.0, 20.0]
    
    def test_express_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.express_transfer(50.0)
        assert company_account.history == [-50.0, -5.0]
    
    def test_express_and_normal_transfer_history(self, company_account):
        company_account.balance = 100.0
        company_account.incoming_transfer(500.0)
        company_account.express_transfer(300.0)
        assert company_account.history == [500.0, -300.0, -5.0]