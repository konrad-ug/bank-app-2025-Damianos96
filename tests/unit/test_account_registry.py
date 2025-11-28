from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount
import pytest

class TestAccountRegistry:
    @pytest.fixture
    def registry(self):
        return AccountRegistry()
    
    @pytest.fixture
    def account(self):
        account = PersonalAccount("John", "Doe", "12345678912")
        return account
    
    @pytest.fixture
    def account2(self):
        account2 = PersonalAccount("John", "Doe", "12345678900")
        return account2
    
    def test_add_and_get_account(self, registry: AccountRegistry, account):
        registry.add_account(account)
        retrieved_account = registry.get_account_by_pesel("12345678912")
        assert retrieved_account == account
    
    def test_get_account_not_found(self, registry: AccountRegistry):
        retrieved_account = registry.get_account_by_pesel("11111111111")
        assert retrieved_account is None
    
    def test_get_all_accounts(self, registry: AccountRegistry, account, account2):
        registry.add_account(account)
        registry.add_account(account2)
        all_accounts = registry.get_all_accounts()
        assert all_accounts == [account, account2]
    
    def test_get_number_of_accounts_1(self, registry: AccountRegistry, account):
        registry.add_account(account)
        number_of_accounts = registry.get_account_count()
        assert number_of_accounts == 1

    def test_get_number_of_accounts_2(self, registry: AccountRegistry, account, account2):
        registry.add_account(account)
        registry.add_account(account2)
        number_of_accounts = registry.get_account_count()
        assert number_of_accounts == 2
    
    def test_delete_account(self, registry: AccountRegistry, account):
        registry.add_account(account)
        result = registry.delete_account("12345678912")
        assert result == True
    
    def test_delete_account_fail(self, registry: AccountRegistry, account):
        result = registry.delete_account("11111111111")
        assert result == False