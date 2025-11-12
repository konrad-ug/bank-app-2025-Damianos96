from src.personal_account import PersonalAccount
import pytest

class TestPersonalLoan:

    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        return account

    def test_accept_3_income_transaction(self, account):
        account.history = [100.0, 200.0, 150.0]
        result = account.submit_for_loan(50.0)
        assert result == True
        assert account.balance == 50.0
    
    def test_decline_3_income_transaction(self, account):
        account.history = [100.0, -200.0, 150.0]
        result = account.submit_for_loan(50.0)
        assert result == False
        assert account.balance == 0.0 

    def test_accept_5_last_transaction(self, account):
        account.history = [100.0, 200.0, -150.0, 150.0, -50.0]
        result = account.submit_for_loan(50.0)
        assert result == True
        assert account.balance == 50.0 
    
    def test_decline_5_last_transaction_too_low_balance_of_transactions(self, account):
        account.history = [100.0, -200.0, 150.0, -200.0, 50.0]
        result = account.submit_for_loan(50.0)
        assert result == False
        assert account.balance == 0.0 

    def test_decline_5_last_transaction_not_enough_transaction(self, account):
        account.history = [100.0, -200.0, 150.0, 200.0]
        result = account.submit_for_loan(50.0)
        assert result == False
        assert account.balance == 0.0 
    
    def test_decline_5_last_transaction_too_much_loan_amount(self, account):
        account.history = [100.0, -200.0, 300.0, -200.0, 50.0]
        result = account.submit_for_loan(1500.0)
        assert result ==  False
        assert account.balance == 0.0 

