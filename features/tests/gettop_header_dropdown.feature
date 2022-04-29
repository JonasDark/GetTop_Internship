# Created by Luttge at 4/26/2022
Feature: GetTop Header Dropdown Choices

  Scenario: iPhone dropdown menu product link verification
      Given Open GetTop home page
      When Hover over product category
      And Verify 4 links present
      Then Click products and verify correct pages open


  Scenario Outline: MACBOOK and ACCESSORIES category dropdowns contain correct products
      Given Open GetTop home page
      When Hover over <category> category
      Then Verify that <product name 1> present
      And Verify that <product name 2> present
      And Verify that <product name 3> present
      When Hover over <category> category
      Then Verify that <product name 1> present
      And Verify that <product name 2> present
      And Verify that <product name 3> present
      Examples:
      |category            |product name 1    |product name 2  |product name 3 |
      |macbook             |macbook-pro-13    |macbook-pro-16  |macbook-air    |
      |accessories/airpods |cases             |airpods         |airpods-pro    |


    Scenario Outline: IPHONE and IPAD category dropdowns contain correct products
       Given Open GetTop home page
       When Hover over <category> category
       Then Verify that <product name 1> present
       And Verify that <product name 2> present
       And Verify that <product name 3> present
       And Verify that <product name 4> present
       When Hover over <category> category
       Then Verify that <product name 1> present
       And Verify that <product name 2> present
       And Verify that <product name 3> present
       And Verify that <product name 4> present
       Examples:
       |category           |product name 1    |product name 2  |product name 3 |product name 4  |
       |iphone             |iphone-12         |iphone-11       |iphone-11pro   |iphone-se       |
       |ipad               |ipad              |ipad-pro        |ipad-mini      |ipad-air        |


    Scenario Outline: WATCH category dropdowns contain correct products
        Given Open GetTop home page
        When Hover over <category> category
        Then Verify that <product name 1> present
        And Verify that <product name 2> present
        Examples:
        |category          |product name 1       |product name 2  |
        |accessories/watch |california-sub-river |jack-jones      |


  Scenario: Product category links connect to correct product category page
    Given Open GetTop home page
    Then Click category links and verify correct page opens

