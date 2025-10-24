from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestTransfersPersonal:
    def test_incoming_transfer(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901") #1. set up
        personal_account.incoming_transfer(100.0) #2. action
        assert personal_account.balance == 100.0 # 3. assertion

    def test_outgoing_transfer(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901") #1. set up
        personal_account.balance = 70.0 #1. set up
        personal_account.outgoing_transfer(50.0) #2. action
        assert personal_account.balance == 20.0 # 3. assertion
    
    def test_outgoing_transfer_insufficient_balance(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.outgoing_transfer(200.0)
        assert personal_account.balance == 100.0
    
    def test_outgoing_transfer_negative(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.outgoing_transfer(-50.0)
        assert personal_account.balance == 100.0
    
    def test_incoming_transfer_negative(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.incoming_transfer(-50.0)
        assert personal_account.balance == 100.0

class TestTransfersFirm:
    def test_incoming_transfer(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.incoming_transfer(100.0)
        assert company_account.balance == 100.0

    def test_outgoing_transfer(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 70.0
        company_account.outgoing_transfer(50.0)
        assert company_account.balance == 20.0
    
    def test_outgoing_transfer_insufficient_balance(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.outgoing_transfer(200.0)
        assert company_account.balance == 100.0
    
    def test_outgoing_transfer_negative(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.outgoing_transfer(-50.0)
        assert company_account.balance == 100.0
    
    def test_incoming_transfer_negative(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.incoming_transfer(-50.0)
        assert company_account.balance == 100.0