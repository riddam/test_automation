from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.support.ui import Select

from ..library.utils import get_table_dict, check_table_data, create_expected_table_sorted

# Scenarios
scenarios('../features/web_sort.feature')


# Given Steps
@given('the CyberSecurity detail page is displayed', target_fixture='original_table_data')
def web_home(browser, element):
    """
    Provide web page and its table data
    :param browser: fixture provides driver instance
    :param element: fixture to take element properties
    :return:
    """
    browser.get(element['webpage'])
    table_object = browser.find_element_by_xpath(element['table'])
    table_data = get_table_dict(table_object)
    return table_data


# Given Steps
@given('the CyberSecurity detail page with "<filter_data>"', target_fixture='original_table_data')
def web_home_filtered(browser, element, filter_data):
    """
    Provide web page with searched text and its table data
    :param browser: fixture provides driver instance
    :param element: fixture to take element properties
    :param filter_data: test data regarding filter text
    :return:
    """
    browser.get(element['webpage'])
    search_input = browser.find_element_by_id(element['filter_data'])
    search_input.send_keys(filter_data)
    table_object = browser.find_element_by_xpath(element['table'])
    table_data = get_table_dict(table_object)
    return table_data


# When Steps
@when(parsers.parse('the user clicked for "<sort_data>"'))
def sort_by_value(browser, element, sort_data):
    """
    functions to take sort action on web page
    :param browser: fixture provides driver instance
    :param element: fixture to take element properties
    :param sort_data: test data regarding sort value
    :return:
    """
    sort_filter = Select(browser.find_element_by_xpath(element['sort_data']))
    sort_filter.select_by_value(sort_data)


# Then Steps
@then(parsers.parse('results are sorted based on "<sort_data>"'))
def sort_results(browser, element, original_table_data, sort_data):
    """
    Test case validation regarding sorted table
    :param browser: fixture provides driver instance
    :param element: fixture to take element properties
    :param original_table_data: fixture providing original web table
    :param sort_data: test data regarding sort value
    :return:
    """
    assert browser.title == 'simplesite'
    actual_table_obj = browser.find_element_by_xpath(element['table'])
    actual_table = get_table_dict(actual_table_obj)
    expected_table = create_expected_table_sorted(original_table=original_table_data, sort_data=sort_data)
    assert check_table_data(actual_table, expected_table)
