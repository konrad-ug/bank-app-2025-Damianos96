from behave import *
import requests

URL = "http://localhost:5000"

use_step_matcher("re")

@step('I create an account using name: "(?P<name>.+)", last name: "(?P<last_name>.+)", pesel: "(?P<pesel>.+)"')
def create_account(context, name, last_name, pesel):
    json_body = {
        "name": name,
        "surname": last_name,
        "pesel": pesel
    }
    create_resp = requests.post(URL + "/api/accounts", json=json_body)
    assert create_resp.status_code == 201

@step('Account registry is empty')
def clear_account_registry(context):
    response = requests.get(URL + "/api/accounts")
    if response.status_code == 200:
        accounts = response.json()
        for account in accounts:
            pesel = account["pesel"]
            requests.delete(URL + f"/api/accounts/{pesel}")
    
    check = requests.get(URL + "/api/accounts/count")
    if check.status_code == 200:
        assert check.json()["count"] == 0

@step('Number of accounts in registry equals: "(?P<count>.+)"')
def is_account_count_equal_to(context, count):
    response = requests.get(URL + "/api/accounts/count")
    assert response.status_code == 200
    assert str(response.json()["count"]) == str(count)

@step('Account with pesel "(?P<pesel>.+)" exists in registry')
def check_account_with_pesel_exists(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200
    assert response.json()["pesel"] == pesel

@step('Account with pesel "(?P<pesel>.+)" does not exist in registry')
def check_account_with_pesel_does_not_exist(context, pesel):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 404

@when('I delete account with pesel: "(?P<pesel>.+)"')
def delete_account(context, pesel):
    response = requests.delete(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200

@when('I update "(?P<field>.+)" of account with pesel: "(?P<pesel>.+)" to "(?P<value>.+)"')
def update_field(context, field, pesel, value):
    if field not in ["name", "surname"]:
        raise ValueError(f"Invalid Field: {field}. Must be 'name' or 'surname'.")
    
    json_body = {field: value}
    response = requests.patch(URL + f"/api/accounts/{pesel}", json=json_body)
    assert response.status_code == 200

@then('Account with pesel "(?P<pesel>.+)" has "(?P<field>.+)" equal to "(?P<value>.+)"')
def field_equals_to(context, pesel, field, value):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    assert response.status_code == 200
    data = response.json()
    
    actual_value = str(data.get(field))
    
    if field == "balance" and actual_value.endswith(".0") and "." not in value:
        actual_value = actual_value[:-2]
        
    assert actual_value == str(value), f"Expected {field} to be {value}, but got {actual_value}"

@step('I make an incoming transfer of "(?P<amount>.+)" to account with pesel "(?P<pesel>.+)"')
def make_incoming_transfer(context, amount, pesel):
    json_body = {
        "type": "incoming",
        "amount": float(amount)
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_response_code = response.status_code

@step('I make an outgoing transfer of "(?P<amount>.+)" from account with pesel "(?P<pesel>.+)"')
def make_outgoing_transfer(context, amount, pesel):
    json_body = {
        "type": "outgoing",
        "amount": float(amount)
    }
    response = requests.post(URL + f"/api/accounts/{pesel}/transfer", json=json_body)
    context.last_response_code = response.status_code

@then('The transfer should fail with status code "(?P<status_code>.+)"')
def check_transfer_failed(context, status_code):
    assert hasattr(context, 'last_response_code'), "No transfer was attempted!"
    assert str(context.last_response_code) == str(status_code)