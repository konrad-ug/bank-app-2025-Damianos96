class FirmAccount:
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if self.is_valid_nip(nip) else "Invalid"
        self.balance = 0.0
    
    def is_valid_nip(self, nip):
        if len(nip) != 10:
            return False
        return True

    def incoming_transfer(self,amount):
        if amount <= 0:
            return
        else:
            self.balance += amount
    
    def outgoing_transfer(self,amount):
        if amount <= 0 or self.balance < amount:
            return
        else:
            self.balance -= amount