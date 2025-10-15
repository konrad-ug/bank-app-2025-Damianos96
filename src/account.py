class Account:
    def __init__(self, first_name, last_name, pesel, promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        self.pesel = pesel if self.is_pesel_valid(pesel) else "Invalid"
        self.promo_code = promo_code if self.is_promo_code_valid(promo_code) else "Invalid"

    def is_pesel_valid(self, pesel):
        if pesel and len(pesel) == 11:
            return True
        return False

    def is_promo_code_valid(self, promo_code):
        if promo_code and promo_code[0:5] == "PROM_" and len(promo_code) >= 8:
            return True
        return False