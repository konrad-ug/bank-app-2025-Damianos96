from .personal_account import PersonalAccount
from typing import List

class AccountRegistry:
    def __init__(self):
        self.accounts: List[PersonalAccount] = []

    def add_account(self, account):
        existing_account = self.get_account_by_pesel(account.pesel)
        if not existing_account:
            self.accounts.append(account)

    def get_account_by_pesel(self, pesel):
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None
    
    def get_all_accounts(self):
        return self.accounts
    
    def get_account_count(self):
        return len(self.accounts)
    
    def delete_account(self, pesel):
        account_to_remove = self.get_account_by_pesel(pesel)
        if account_to_remove:
            self.accounts.remove(account_to_remove)
            return True
        return False