class Account:
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