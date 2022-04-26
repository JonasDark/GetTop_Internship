# Created by Luttge at 4/21/2022

Feature: Tests for GetTop Wishlist page

  Scenario: Add iPhone SE product to wishlist
    Given Open GetTop main page
    When Open iPhone SE product page
    And Add product to wishlist
    And Open wishlist page
    Then Verify iPhone SE added to wishlist


  Scenario: Remove product from wishlist
    Given Open GetTop ipad-mini product page
    When Add product to wishlist
    And Open wishlist page
    Then Remove product from wishlist
    And Verify removal message


  Scenario: Wishlist product link functional
    Given Open GetTop airpods-pro product page
    When Add product to wishlist
    And Open wishlist page
    And Click product item link in wishlist
    Then Verify AirPods Pro product page opens


  Scenario: Verify social media logos present on wishlist page
    Given Open GetTop iphone-11 product page
    When Add product to wishlist
    And Open wishlist page
    Then Verify social media logos present



