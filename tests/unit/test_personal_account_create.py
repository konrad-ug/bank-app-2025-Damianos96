from src.personal_account import PersonalAccount

class TestPersonalAccount:
    def test_PersonalAccount_creation(self):
        personal_account = PersonalAccount("John", "Doe", "12345678912")
        assert personal_account.first_name == "John"
        assert personal_account.last_name == "Doe"
        assert personal_account.balance == 0.0

    def test_pesel_too_long(self):
        personal_account = PersonalAccount("Jane", "Smith", "198421941984149")
        assert personal_account.pesel == "Invalid"
    
    def test_pesel_too_short(self):
        personal_account = PersonalAccount("Jane", "Smith", "21313")
        assert personal_account.pesel == "Invalid"
    
    def test_pesel_empty(self):
        personal_account = PersonalAccount("Jane", "Smith", "")
        assert personal_account.pesel == "Invalid"

    def test_valid_promo_code(self):
        personal_account = PersonalAccount("Jane", "Smith", "04295678910", "PROM_ABC")
        assert personal_account.balance == 50.0
    
    def test_invalid_code_prefix(self):
        personal_account = PersonalAccount("Jane", "Smith", "12345678910", "PRxM_ab1")
        assert personal_account.balance == 0.0
    
    def test_invalid_code_suffix(self):
        personal_account = PersonalAccount("Jane", "Smith", "12345678910", "PRxM_ab1")
        assert personal_account.balance == 0.0
    
    def test_valid_code_age(self):
        personal_account = PersonalAccount("Jane", "Smith", "04295678910", "PROM_ab1")
        assert personal_account.balance == 50.0
    
    def test_invalid_code_age(self):
        personal_account = PersonalAccount("Jane", "Smith", "12105678910", "PROM_ab1")
        assert personal_account.balance == 0.0
    
class TestGetBirthYearFromPesel:
    def test_get_birth_year_from_pesel_too_short(self):
        personal_account = PersonalAccount("Jane", "Smith", "12105678910", "PROM_ab1")
        assert personal_account.get_birth_year_from_pesel("123") == 0
    
    def test_get_birth_year_from_pesel_invalid(self):
        personal_account = PersonalAccount("Jane", "Smith", "12105678910", "PROM_ab1")
        assert personal_account.get_birth_year_from_pesel("99550112345") == 0