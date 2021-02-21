from pytest_bdd import scenarios, given, when, then, parsers

from ..library.utils import get_table_dict, check_table_data, create_expected_table_search

# Scenarios
scenarios('../features/web_filter.feature')


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


# When Steps
@when(parsers.parse('the user search for "<filter_data>"'))
def search_phrase(browser, element, filter_data):
    """
    functions to take search action on web page
    :param browser: fixture provides driver instance
    :param element: fixture to take element properties
    :param filter_data: test data regarding filter text
    :return:
    """
    search_input = browser.find_element_by_id(element['filter_data'])
    search_input.send_keys(filter_data)


# Then Steps
@then(parsers.parse('results are filter based on "<filter_data>"'))
def search_results(browser, element, original_table_data, filter_data):
    """
    Test case validation regarding searched table
    :param browser: fixture provides driver instance
    :param element: fixture to take element properties
    :param original_table_data: fixture providing original web table
    :param filter_data: test data regarding filter text
    :return:
    """
    assert browser.title == 'simplesite'
    actual_table_obj = browser.find_element_by_xpath(element['table'])
    actual_table = get_table_dict(actual_table_obj)
    expected_table = create_expected_table_search(original_table=original_table_data, search_data=filter_data)
    assert check_table_data(actual_table, expected_table)
