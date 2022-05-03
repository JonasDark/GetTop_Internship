# Created by Luttge at 5/2/2022
Feature: GetTop product category page products

  Scenario: 1 - Only items of correct category shown
    Given Open iPhone category page
    Then Verify only IPHONE category products are displayed

  Scenario: 2 - Correct amount of results displayed
    Given Open iPad category page
    Then Verify amount of products displayed matches showing result digit

  Scenario: 3 - All products have a category, name, and price listed
    Given Open macbook category page
    Then Verify product category label present
    And Verify product name present
    And Verify product price present
    #Then Verify product has a category, name, and price

  Scenario: 4 - Quickview can be opened by clicking image and closed by clicking 'X'
    Given Open iPad category page
    Then Open and close quickview for each product on page

  Scenario: 5 - Verify user can add product to cart from quickview
    Given Open iPhone category page
    When Open quickview for each product on page and add to cart
    Then verify correct number of items added to cart