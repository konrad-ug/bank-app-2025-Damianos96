from src.firm_account import FirmAccount

class TestTransfers:
    def test_incoming_transfer(self):
        firm_account = FirmAccount("Microsoft", "1231231231")
        firm_account.incoming_transfer(100.0)
        assert firm_account.balance == 100.0

    def test_outgoing_transfer(self):
        firm_account = FirmAccount("Microsoft", "1231231231")
        firm_account.balance = 70.0
        firm_account.outgoing_transfer(50.0)
        assert firm_account.balance == 20.0
    
    def test_outgoing_transfer_insufficient_balance(self):
        firm_account = FirmAccount("Microsoft", "1231231231")
        firm_account.balance = 100.0
        firm_account.outgoing_transfer(200.0)
        assert firm_account.balance == 100.0
    
    def test_outgoing_negative_transfer(self):
        firm_account = FirmAccount("Microsoft", "1231231231")
        firm_account.balance = 100.0
        firm_account.outgoing_transfer(-50.0)
        assert firm_account.balance == 100.0
    
    def test_incoming_negative_transfer(self):
        firm_account = FirmAccount("Microsoft", "1231231231")
        firm_account.balance = 100.0
        firm_account.incoming_transfer(-50.0)
        assert firm_account.balance == 100.0