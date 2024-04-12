# Created by apkau at 4/10/2024
Feature:Test for Target main Page UI
  # Enter feature description here

  Scenario: Verify header is shown
    Given Open Target main page
    Then Verify header is shown

  Scenario: Verify header has correct account links
    Given Open Target main page
    Then Verify header has 6 links
