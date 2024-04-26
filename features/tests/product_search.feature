Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
 #   And Click on search icon
  #  Then Product results for Car are shown

  Scenario: User can select color of product
    Given open target product {91511634} page
    Then User can click on colors

Scenario: Verify product have name and image
  Given Open Target main page
  When Search for "mango"
 Then verify product name and image



