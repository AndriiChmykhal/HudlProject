# Hudl Web Automation

## Quick Start

### Setup

#### Prerequisites
- Install Python 3.10 or later
- Install Google Chrome and Safari browsers
- Install `pip` and `virtualenv`
- Create a `.env` file in the root of the project

### Configuration
- **Valid credentials**: Before running authentication tests, ensure you update `valid_email` and `valid_password` in `.env`.
- **Test markers**: Use `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.p0`, `@pytest.mark.p1`, etc., to categorize their association with test suites

### Running Tests

#### Run tests on Chrome
```sh
pytest src/tests/ --browser=chrome
```

#### Run tests on Safari
```sh
pytest src/tests/ --browser=safari
```

#### Run tests on both browsers
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


