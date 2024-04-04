# Created by apkau at 4/4/2024
Feature: Search cart in Target
  # Enter feature description here
  Scenario: check cart is empty
  Given Open Target main page
  When Check for shopping cart
  Then  Verify the cart is empty

  Scenario: Verify logged out user can sign in
    Given open Target main page
    When User can Sign in
    Then Verify Sign In form opened