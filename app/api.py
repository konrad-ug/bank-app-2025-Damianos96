from flask import Flask, request, jsonify
from src.account_registry import AccountRegistry
from src.personal_account import PersonalAccount

app = Flask(__name__)
registry = AccountRegistry()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account = PersonalAccount(data["name"], data["surname"], data["pesel"])
    success = registry.add_account(account)
    if success:
        return jsonify({"message": "Account created"}), 201
    else:
        return jsonify({"message": "Account with this pesel already exists"}), 409

@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel":
    acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    accounts = registry.get_all_accounts()
    count = len(accounts)
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    print(f"Get account request for PESEL: {pesel}")
    acc = registry.get_account_by_pesel(pesel)
    if acc:
        return jsonify({
            "name": acc.first_name,
            "surname": acc.last_name,
            "pesel": acc.pesel,
            "balance": acc.balance
        }), 200
            
    return jsonify({"message": "Account not found"}), 404

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    print(f"Update account request for PESEL: {pesel}")
    data = request.get_json()
    acc = registry.get_account_by_pesel(pesel)
    if acc:
        if "name" in data:
            acc.first_name = data["name"]
        if "surname" in data:
            acc.last_name = data["surname"]
        return jsonify({"message": "Account updated"}), 200
    return jsonify({"message": "Account not found"}), 404

@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    print(f"Delete account request for PESEL: {pesel}")
    if registry.delete_account(pesel):
        return jsonify({"message": "Account deleted"}), 200          
    return jsonify({"message": "Account not found"}), 404