from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount
import pytest
class TestTransfersPersonal:
    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678901") #1. set up
        return account
    
    def test_incoming_transfer(self, account):
        account.incoming_transfer(100.0) #2. action
        assert account.balance == 100.0 # 3. assertion

    def test_outgoing_transfer(self, account):
        account.balance = 70.0 #1. set up
        account.outgoing_transfer(50.0) #2. action
        assert account.balance == 20.0 # 3. assertion
    
    def test_outgoing_transfer_insufficient_balance(self, account):
        account.balance = 100.0
        account.outgoing_transfer(200.0)
        assert account.balance == 100.0
    
    def test_outgoing_transfer_negative(self, account):
        account.balance = 100.0
        account.outgoing_transfer(-50.0)
        assert account.balance == 100.0
    
    def test_incoming_transfer_negative(self, account):
        account.balance = 100.0
        account.incoming_transfer(-50.0)
        assert account.balance == 100.0

class TestTransfersCompany:
    @pytest.fixture
    def company_account(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        return company_account
    
    def test_incoming_transfer(self, company_account):
        company_account.incoming_transfer(100.0)
        assert company_account.balance == 100.0

    def test_outgoing_transfer(self, company_account):
        company_account.balance = 70.0
        company_account.outgoing_transfer(50.0)
        assert company_account.balance == 20.0
    
    def test_outgoing_transfer_insufficient_balance(self, company_account):
        company_account.balance = 100.0
        company_account.outgoing_transfer(200.0)
        assert company_account.balance == 100.0
    
    def test_outgoing_transfer_negative(self, company_account):
        company_account.balance = 100.0
        company_account.outgoing_transfer(-50.0)
        assert company_account.balance == 100.0
    
    def test_incoming_transfer_negative(self, company_account):
        company_account.balance = 100.0
        company_account.incoming_transfer(-50.0)
        assert company_account.balance == 100.0