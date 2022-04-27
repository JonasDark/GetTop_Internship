# Created by Luttge at 4/26/2022
Feature: GetTop Header Dropdown Choices

  Scenario: iPhone dropdown menu product link verification
      Given Open GetTop home page
      When Hover over product category
      And Verify 4 links present
      Then Click products and verify correct pages open
