@web @sort
Feature: Testing of CyberSecurity web page sort functionality
  As a user,
  I want to sort information about cyber security attacks based on available parameters,
  So I can get new information as soon as possible.

  Background:
    Given the CyberSecurity detail page is displayed

  Scenario Outline: Sort the details by sort data
    When the user clicked for "<sort_data>"
    Then results are sorted based on "<sort_data>"

    Examples:
      | sort_data     |
      | name          |
      | cases         |
      | averageImpact |
      | complexity    |

  @filtersort
  Scenario Outline: Sort the searched details by sort data
    Given the CyberSecurity detail page with "<filter_data>"
    When the user clicked for "<sort_data>"
    Then results are sorted based on "<sort_data>"
    Examples:
      | sort_data     | filter_data |
      | name          | in          |
      | cases         | high        |
      | averageImpact | 1           |
      | complexity    | h           |