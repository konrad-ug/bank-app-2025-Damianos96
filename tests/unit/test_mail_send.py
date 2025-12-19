import pytest
from unittest.mock import patch
from datetime import date
from src.personal_account import PersonalAccount
from src.company_account import CompanyAccount

class TestMailSending:

    @patch('src.personal_account.SMTPClient')
    def test_send_email_personal_account_success(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        mock_smtp_instance.send.return_value = True

        account = PersonalAccount("Jan", "Kowalski", "123456789")
        account.history = [100, -50, 200]
        email = "jan@test.pl"

        result = account.send_history_via_email(email)

        assert result is True
        
        today = date.today().strftime("%Y-%m-%d")
        expected_subject = f"Account Transfer History {today}"
        expected_content = "Personal account history: [100, -50, 200]"
        
        mock_smtp_instance.send.assert_called_once_with(
            expected_subject, 
            expected_content, 
            email
        )

    @patch('src.personal_account.SMTPClient')
    def test_send_email_personal_account_failure(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        mock_smtp_instance.send.return_value = False

        account = PersonalAccount("Jan", "Kowalski", "123456789")
        email = "jan@test.pl"

        result = account.send_history_via_email(email)

        assert result is False
        mock_smtp_instance.send.assert_called_once()

    @patch('src.company_account.SMTPClient')
    def test_send_email_company_account(self, MockSMTP):
        with patch.object(CompanyAccount, '_check_nip_in_gov', return_value=True):
            account = CompanyAccount("Firma", "1234567890")
            account.history = [5000, -100]
        
        mock_smtp_instance = MockSMTP.return_value
        mock_smtp_instance.send.return_value = True
        email = "firma@test.pl"

        result = account.send_history_via_email(email)

        assert result is True
        
        today = date.today().strftime("%Y-%m-%d")
        expected_subject = f"Account Transfer History {today}"
        expected_content = "Company account history: [5000, -100]"

        mock_smtp_instance.send.assert_called_once_with(
            expected_subject,
            expected_content,
            email
        )
    
    @patch('src.company_account.SMTPClient')
    def test_send_email_company_account_failure(self, MockSMTP):
        with patch.object(CompanyAccount, '_check_nip_in_gov', return_value=True):
            account = CompanyAccount("Firma", "1234567890")
        
        mock_smtp_instance = MockSMTP.return_value
        mock_smtp_instance.send.return_value = False
        
        email = "firma@test.pl"

        result = account.send_history_via_email(email)

        assert result is False
        
        mock_smtp_instance.send.assert_called_once()