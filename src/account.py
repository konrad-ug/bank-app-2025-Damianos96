class Account:
    def __init__(self, first_name, last_name, pesel, promo_code = None):
        self.first_name = first_name
        self.last_name = last_name
        self.pesel = pesel if self.is_pesel_valid(pesel)  else "Invalid"
        self.balance = 50.0 if self.pesel != "Invalid" and self.is_promo_code_valid(promo_code) and self.get_birth_year_from_pesel(pesel) > 1960 else 0.0

    def is_pesel_valid(self, pesel):
        if pesel and len(pesel) == 11:
            return True
        return False

    def is_promo_code_valid(self, promo_code):
        if promo_code and promo_code.startswith("PROM_") and len(promo_code) == 8:
            return True
        return False
    
    def get_birth_year_from_pesel(self,pesel):
        if len(pesel) != 11:
            return 0
        YY = int(pesel[0:2])
        MM = int(pesel[2:4])
        if 1 <= MM <= 12:
            base = 1900
            return base + YY
        elif 21 <= MM <= 32:
            base = 2000
            return base + YY
        elif 41 <= MM <= 52:
            base = 2100
            return base + YY
        elif 61 <= MM <= 72:
            base = 2200
            return base + YY
        elif 81 <= MM <= 92:
            base = 1800
            return base + YY
        else:
            return 0

    