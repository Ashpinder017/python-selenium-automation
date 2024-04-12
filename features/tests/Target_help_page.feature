# Created by apkau at 4/12/2024
Feature:Test for Target Help page
#Enter feature name here
  # Enter feature description here

  Scenario: Verify Help Hearder is shown
    Given open the Target Help page
    Then Verify Target help header is shown
    When Verify there is search help box
    Then Verify there is search icon
    Then Verify there is 6 links to search
    Then Verify there is contact us link
    Then Verify there is link to browse all help pages
