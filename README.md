# Hudl Web Automation

## Overview
Hudl Web Automation is a test automation project built using **Python** and **Selenium WebDriver**.

## Quick Start

### Setup

#### Prerequisites
- Install Python 3.10 or later
- Install Google Chrome and Safari browsers
- Install `pip` and `virtualenv`
- - Install Selenium:
  ```sh
  pip install selenium
  ```
- Install `psutil`
  ```sh
  pip install psutil
  ```
- Update `valid_email` and `valid_password` in `.env`

### Supported Browsers
- **Google Chrome**
- **Safari** (Must be run on macOS)


#### **Safari Setup Requirement**
Enable remote automation in Safari:
1. Go to **Settings → Advanced** and enable **"Show Develop menu in menu bar"**
2. Open **Develop menu** and enable **"Allow Remote Automation"**
3. Restart Safari before running tests

### Configuration
- **Test markers**: Use `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.p0`, `@pytest.mark.p1`, etc., to categorize test case priorities and their association with  test suites

### Running Tests

#### Run tests on Chrome
```sh
pytest src/tests/ --browser=chrome
```

#### Run tests on Safari (macOS only)
```sh
pytest src/tests/ --browser=safari
```

#### Run tests on both browsers (macOS only)
```sh
pytest src/tests/ --browser=chrome --browser=safari
```

#### Run a specific test
```sh
pytest src/tests/test_login.py::test_login_with_valid_credentials --browser=chrome
```


### Reporting

**Pytest HTML Report**:
  ```sh
  pytest src/tests/ --browser=chrome --html=report.html


