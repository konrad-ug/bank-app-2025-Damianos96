from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestPersonalTransferHistory:
    def test_incoming_transfer_history(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.incoming_transfer(50.0)
        assert personal_account.history == [50.0]
    
    def test_double_incoming_transfer_history(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.incoming_transfer(50.0)
        personal_account.incoming_transfer(20.0)
        assert personal_account.history == [50.0, 20.0]
    
    def test_outgoing_transfer_history(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.outgoing_transfer(50.0)
        assert personal_account.history == [-50.0]
    
    def test_double_outgoing_transfer_history(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.outgoing_transfer(50.0)
        personal_account.outgoing_transfer(20.0)
        assert personal_account.history == [-50.0, -20.0]

    def test_mixed_transfer_history(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.outgoing_transfer(50.0)
        personal_account.incoming_transfer(20.0)
        assert personal_account.history == [-50.0, 20.0]
    
    def test_express_transfer_history(self):
        personal_account = PersonalAccount("John", "Doe", "12345678901")
        personal_account.balance = 100.0
        personal_account.express_transfer(50.0)
        assert personal_account.history == [-50.0, -1.0]

class TestCompanyTransferHistory:
    def test_incoming_transfer_history(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.incoming_transfer(50.0)
        assert company_account.history == [50.0]
    
    def test_double_incoming_transfer_history(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.incoming_transfer(50.0)
        company_account.incoming_transfer(20.0)
        assert company_account.history == [50.0, 20.0]
    
    def test_outgoing_transfer_history(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.outgoing_transfer(50.0)
        assert company_account.history == [-50.0]
    
    def test_double_outgoing_transfer_history(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.outgoing_transfer(50.0)
        company_account.outgoing_transfer(20.0)
        assert company_account.history == [-50.0, -20.0]

    def test_mixed_transfer_history(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.outgoing_transfer(50.0)
        company_account.incoming_transfer(20.0)
        assert company_account.history == [-50.0, 20.0]
    
    def test_express_transfer_history(self):
        company_account = CompanyAccount("Microsoft", "1231231231")
        company_account.balance = 100.0
        company_account.express_transfer(50.0)
        assert company_account.history == [-50.0, -5.0]