import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Registers the --browser option with pytest"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome or safari"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()

    match browser:
        case "chrome":
            driver = webdriver.Chrome()
        case "safari":
            driver = webdriver.Safari()
        case _:
            raise ValueError(f"Unsupported browser: {browser}. Use 'chrome' or 'safari'.")

    driver.maximize_window()
    yield driver
    driver.quit()
