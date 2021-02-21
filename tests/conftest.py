"""
This module contains shared fixtures, steps, and hooks.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOpt
from selenium.webdriver.firefox.options import Options as firefoxOpt
import json
import pathlib


# Hook
def pytest_addoption(parser):
    parser.addoption(
        "--driver", action="store", default="firefox", help="DRIVER: firefox or chrome"
    )


# Fixtures
@pytest.fixture(scope="session")
def browser(request):
    driver_type = request.config.getoption("--driver")

    if driver_type == 'chrome':
        options = chromeOpt()
        options.add_argument("--headless")
        b = webdriver.Chrome(chrome_options=options)
    else:
        options = firefoxOpt()
        options.add_argument("--headless")
        b = webdriver.Firefox(firefox_options=options)
    b.implicitly_wait(3)
    # b.maximize_window()
    yield b
    b.quit()


@pytest.fixture(scope="session")
def element():
    path = pathlib.Path(__file__).parent
    with open(f'{path}/web_elements.json', 'r') as fp:
        element_dict = json.load(fp)
        yield element_dict


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
