from .account import Account

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__(0.0)
        self.company_name = company_name
        self.nip = nip if self.is_valid_nip(nip) else "Invalid"
    
    def is_valid_nip(self, nip):
        if nip and len(nip) == 10:
            return True
        return False