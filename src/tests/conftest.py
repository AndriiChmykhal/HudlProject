import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use for tests")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")

    match browser:
        case "chrome":
            driver = webdriver.Chrome()
        case "safari":
            driver = webdriver.Safari()
        case _:
            raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    yield driver

    driver.quit()
