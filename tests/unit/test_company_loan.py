from src.company_account import CompanyAccount
import pytest

class TestCompanyLoan:

    @pytest.fixture
    def company_account(self):
        return CompanyAccount("Microsoft", "1231231231")

    @pytest.mark.parametrize("history, initial_balance, loan_amount, expected_result, expected_final_balance", [
        ([10.0, -1775.0, 2000.0], 500.0, 100.0, True, 600.0),
        ([10.0, -1775.0, 2000.0], 500.0, 260.0, False, 500.0),
        ([10.0, 1750.0, 2000.0], 500.0, 100.0, False, 500.0),
        ([10.0, 1750.0, 2000.0], 500.0, 260.0, False, 500.0)
    ], ids = [
        "correct ZUS, correct balance",
        "correct ZUS, incorrect balance",
        "incorrect ZUS, correct balance",
        "incorrect ZUS, incorrect balance"
    ])
    def test_take_loan(self, company_account, history, initial_balance, loan_amount, expected_result, expected_final_balance):
        company_account.history = history
        company_account.balance = initial_balance
        result = company_account.take_loan(loan_amount)
        assert result == expected_result
        assert company_account.balance == expected_final_balance