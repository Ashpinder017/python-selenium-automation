# Created by apkau at 4/4/2024
Feature: Search cart in Target
  # Enter feature description here
  Scenario:Verify the cart have items
    Given Open Target main page
    When search for 'pens'
    When click on search icon
    Then select an product
    Then check there is product and price in the cart


  Scenario: Verify logged out user can sign in
    Given open Target main page
    When User can Sign in
    Then Verify Sign In form opened

  Scenario Outline: Verify Target search cases with Behave variabless
    Given Open Target main page
    When Search an <item>
    When Click on search icon
    Then  Verify correct <result> shown
    # And page URl has item details
    Examples:
    |item   | result    |
    |pen    | "pen"     |
    |tea    | "tea"     |
    |water  |"water"    |

  Scenario: check cart is empty
  Given Open Target main page
  When Check for shopping cart
  Then  Verify the cart is empty