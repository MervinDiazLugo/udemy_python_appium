# Created by Mervin at 18/8/2021
Feature: First appium test
  # Enter feature description here

  Scenario: test Scenario
    Given Start application in default device
    Then Close application

  Scenario: Scenario hardcoded
    Given Application start with device Pixel10
    When I set <YOURNAME> and <HERNAME> in LoveMain Page
        |YOURNAME   |HERNAME   |
        |Mervin     | Maria    |
    And wait 10 seconds
    Then Close application