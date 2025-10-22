from src.account import Account

class TestTransfers:
    def test_incoming_transfer(self):
        account = Account("John", "Doe", "12345678901") #1. set up
        account.incoming_transfer(100.0) #2. action
        assert account.balance == 100.0 # 3. assertion

    def test_outgoing_transfer(self):
        account = Account("John", "Doe", "12345678901") #1. set up
        account.balance = 70.0 #1. set up
        account.outgoing_transfer(50.0) #2. action
        assert account.balance == 20.0 # 3. assertion
    
    def test_outgoing_transfer_insufficient_balance(self):
        account = Account("John", "Doe", "12345678901")
        account.balance = 100.0
        account.outgoing_transfer(200.0)
        assert account.balance == 100.0
    
    def test_outgoing_negative_transfer(self):
        account = Account("John", "Doe", "12345678901")
        account.balance = 100.0
        account.outgoing_transfer(-50.0)
        assert account.balance == 100.0
    
    def test_incoming_negative_transfer(self):
        account = Account("John", "Doe", "12345678901")
        account.balance = 100.0
        account.incoming_transfer(-50.0)
        assert account.balance == 100.0