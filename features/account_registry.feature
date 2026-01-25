Feature: Account registry

  Background:
    Given Account registry is empty

  Scenario: User is able to create 2 accounts
    When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
    And I create an account using name: "tadeusz", last name: "szcześniak", pesel: "79101011234"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "89092909246" exists in registry
    And Account with pesel "79101011234" exists in registry

  Scenario: User is able to update surname of already created account
    Given I create an account using name: "nata", last name: "haydamaky", pesel: "95092909876"
    When I update "surname" of account with pesel: "95092909876" to "filatov"
    Then Account with pesel "95092909876" has "surname" equal to "filatov"

  Scenario: Created account has all fields correctly set
    When I create an account using name: "jan", last name: "kowalski", pesel: "12345678901"
    Then Account with pesel "12345678901" exists in registry
    And Account with pesel "12345678901" has "name" equal to "jan"
    And Account with pesel "12345678901" has "surname" equal to "kowalski"
    And Account with pesel "12345678901" has "balance" equal to "0"

  Scenario: User is able to delete created account
    Given I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    When I delete account with pesel: "01092909876"
    Then Account with pesel "01092909876" does not exist in registry
    And Number of accounts in registry equals: "0"

  # Scenariusze do punktu 6c (Przelewy)
  Scenario: User can make an incoming transfer (deposit)
    Given I create an account using name: "elon", last name: "musk", pesel: "55555555555"
    When I make an incoming transfer of "1000" to account with pesel "55555555555"
    Then Account with pesel "55555555555" has "balance" equal to "1000"

  Scenario: User can make an outgoing transfer
    Given I create an account using name: "jeff", last name: "bezos", pesel: "66666666666"
    And I make an incoming transfer of "500" to account with pesel "66666666666"
    When I make an outgoing transfer of "200" from account with pesel "66666666666"
    Then Account with pesel "66666666666" has "balance" equal to "300"

  Scenario: Outgoing transfer fails when insufficient funds
    Given I create an account using name: "broke", last name: "guy", pesel: "11111111111"
    When I make an outgoing transfer of "100" from account with pesel "11111111111"
    Then The transfer should fail with status code "422"
    And Account with pesel "11111111111" has "balance" equal to "0"