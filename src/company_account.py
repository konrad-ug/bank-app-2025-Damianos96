import os
import requests
from datetime import date
from .account import Account
from src.smtp.smtp_client import SMTPClient

class CompanyAccount(Account):
    def __init__(self, company_name, nip):
        super().__init__(0.0)
        self.account_type = "company"
        self.company_name = company_name
        self.nip = nip
        if len(nip) == 10:
            is_verified = self._check_nip_in_gov(nip)
            if not is_verified:
                raise ValueError("Company not registered!!")
    
    def _check_nip_in_gov(self, nip):
        base_url = os.getenv("BANK_APP_MF_URL", "https://wl-test.mf.gov.pl/")
        if not base_url.endswith('/'):
            base_url += '/'
            
        today = date.today().strftime("%Y-%m-%d")
        url = f"{base_url}api/search/nip/{nip}?date={today}"

        try:
            print(f"Sending request to: {url}")
            response = requests.get(url, timeout=5)

            print(f"Response from MF: {response.text}")

            if response.status_code == 200:
                data = response.json()
                subject = data.get("result", {}).get("subject")
                
                if subject and subject.get("statusVat") == "Czynny":
                    return True
            
            return False

        except requests.RequestException as e:
            print(f"Error connecting to MF API: {e}")
            return False
    
    def take_loan(self, amount):
        if (self.balance >= 2*amount) and (-1775.0 in self.history):
            self.balance += amount
            return True
        else:
            return False
        
    def send_history_via_email(self, email_address):
        today = date.today().strftime("%Y-%m-%d")
        subject = f"Account Transfer History {today}"
        text = f"Company account history: {self.history}"
        
        smtp = SMTPClient()
        return smtp.send(subject, text, email_address)