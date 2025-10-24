class Account:
    def __init__(self, balance=0.0):
        self.balance = balance

    def incoming_transfer(self,amount):
        if amount > 0:
            self.balance += amount
    
    def outgoing_transfer(self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
    
    def express_transfer(self, amount):
        if amount > 0 and self.balance >= amount:
            fee = 1.0 if self.account_type == "personal" else 5.0
            self.balance -= amount + fee