from pymongo import MongoClient
import os
from src.personal_account import PersonalAccount

class MongoAccountsRepository:
    def __init__(self):
        host = os.getenv('DB_HOST', 'localhost')
        port = int(os.getenv('DB_PORT', 27017))
        
        self.client = MongoClient(host, port)
        self.db = self.client.bank_db
        self.collection = self.db.accounts

    def save_all(self, accounts):
        self.collection.delete_many({})
        
        for account in accounts:
            self.collection.update_one(
                {"pesel": account.pesel},
                {"$set": account.to_dict()},
                upsert=True
            )

    def load_all(self):
        accounts_data = self.collection.find({})
        loaded_accounts = []
        
        for data in accounts_data:
            account = PersonalAccount(
                data["first_name"], 
                data["last_name"], 
                data["pesel"]
            )
            account.balance = data["balance"]
            account.history = data["history"]
            loaded_accounts.append(account)
            
        return loaded_accounts