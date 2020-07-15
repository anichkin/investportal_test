#Feature: Test navigation between pages
#
#  Scenario: Homepage can go to tenders
#    Given I am on the homepage
#    When I click on the tenders link
#    Then I am on the engtenders page
#
#
#
#  Scenario: Homepage of investportal
#    Given I am on the homepage
#    When I click on the menu button
#    And I checked menu's names
#    And I click on the menu button
#    And I go to the online services
#    Then I check number of complaints
#
#  Scenario: Registration
#    Given I am on the homepage
#    When I click on the account button
#    And I click on the registration button
#    And Scroll frame window
#    And I wait to agreement button
#    And I click on the agreement button
#    Then I am on the registration page
#
#
#
#  Scenario: Account page
#    Given I am on the homepage
#    When I click on the account button
#    And I wrote credits in form
#    And I click to enter
#    Then I am on the account page
#
#
#   Scenario: Create project in DGP
#     Given Authorization in dgp
#     When I click on "create project" button
#     And I fill the forms
#     And I save the project
#     And I wait, when the project will be created
#     Then I delete the project