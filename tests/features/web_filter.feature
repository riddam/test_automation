@web @filter
Feature: Testing of CyberSecurity web page search functionality
  As a web user,
  I want to search information about cyber security attacks based on available parameters,
  So I can get new information as soon as possible.

  Background:
    Given the CyberSecurity detail page is displayed

  Scenario Outline: search the details by text
    When the user search for "<filter_data>"
    Then results are filter based on "<filter_data>"

    Examples:
      | filter_data |
      | in          |
      | nam         |
      | 1           |
      | high        |
      | h           |