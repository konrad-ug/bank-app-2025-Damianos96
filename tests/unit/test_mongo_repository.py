import unittest
from unittest.mock import MagicMock, patch
from src.mongo_accounts_repository import MongoAccountsRepository
from src.personal_account import PersonalAccount

class TestMongoAccountsRepository(unittest.TestCase):
    
    @patch('src.mongo_accounts_repository.MongoClient')
    def setUp(self, mock_client):
        self.mock_db = mock_client.return_value.bank_db
        self.mock_collection = self.mock_db.accounts
        
        self.repo = MongoAccountsRepository()

    def test_save_all(self):
        account1 = PersonalAccount("Jan", "Kowalski", "12345678901")
        account2 = PersonalAccount("Anna", "Nowak", "98765432109")
        accounts = [account1, account2]

        self.repo.save_all(accounts)

        self.repo.collection.delete_many.assert_called_once_with({})
        
        self.assertEqual(self.repo.collection.update_one.call_count, 2)
        
        args, kwargs = self.repo.collection.update_one.call_args_list[0]
        self.assertEqual(args[0], {"pesel": "12345678901"})
        self.assertEqual(args[1]["$set"]["first_name"], "Jan")
        self.assertTrue(kwargs['upsert'])

    def test_load_all(self):
        mock_data = [
            {
                "first_name": "Jan",
                "last_name": "Kowalski",
                "pesel": "12345678901",
                "balance": 100.0,
                "history": [100.0]
            },
            {
                "first_name": "Anna",
                "last_name": "Nowak",
                "pesel": "98765432109",
                "balance": 200.0,
                "history": [200.0]
            }
        ]
        self.repo.collection.find.return_value = mock_data

        loaded_accounts = self.repo.load_all()

        self.assertEqual(len(loaded_accounts), 2)
        self.assertEqual(loaded_accounts[0].first_name, "Jan")
        self.assertEqual(loaded_accounts[0].balance, 100.0)
        self.assertEqual(loaded_accounts[1].pesel, "98765432109")