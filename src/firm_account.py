from src.account import Account

class FirmAccount:
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if self.is_valid_nip(nip) else "Invalid"
        self.balance = 0.0
    
    def is_valid_nip(self, nip):
        if nip and len(nip) == 10:
            return True
        return False