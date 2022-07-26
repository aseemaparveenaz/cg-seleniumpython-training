@high
Feature: Payment process
@creditpayment
  Scenario: Credit card transaction
    Given user is on credit card payment screen new
@debitpayment @creditpayment
  Scenario: Debit card transaction
    Given user is on debit card payment screen new
  Scenario: Cheque transaction
    Given user is on cheque payment screen new