# Automated Test Suite for Automation Exercise

This repository contains an automated test suite designed to verify the functionality of the Automation Exercise web application. The tests cover various aspects of the application, including user registration, login, product searching, and cart management.

## Features

- User Registration
- User Login
- Product Search
- Cart Management
- Checkout Process
- Review Submission
- Subscription Verification
- Brand Navigation
- Address Verification

## Prerequisites

Ensure that you have the following installed on your machine:

- Python 3.x
- Node.js (for package management)
- pip (Python package installer)
- Playwright
- pytest
- Allure Commandline

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:

   ```bash
   playwright install
   ```

4. Install Allure Commandline:

   If you have Java installed, you can install Allure using the following command:

   ```bash
   scoop install allure # On Windows with Scoop
   # or
   brew install allure # On macOS with Homebrew
   ```

## Running Tests

You can run the tests using `pytest` with different browser options. The following commands will allow you to run tests in headless mode on various browsers.

### Run Tests in Firefox

```bash
pytest tests -n 4 --browser=firefox
```

### Run Tests in Chrome

```bash
pytest tests -n 4 --browser=chrome
```

### Run Tests in WebKit (Safari)

```bash
pytest tests -n 4 --browser=webkit
```

### Run All Tests in All Browsers

You can also run the tests in all browsers by simply omitting the `--browser` option:

```bash
pytest tests -n 4
```

## Generating Reports

### Generate Allure Report

After running your tests, you can generate an Allure report using the following commands:

1. **Run your tests with Allure**:

   ```bash
   pytest tests --alluredir=allure-results
   ```

2. **Generate the Allure report**:

   ```bash
   allure generate allure-results --clean -o allure-report
   ```

3. **Serve the report in a local web server**:

   ```bash
   allure serve allure-results
   ```

   This will open the generated report in your default web browser.

## Slack Notifications

Notifications for test results can be sent to Slack using a configured webhook. Please ensure you have the Slack CLI installed and set up.

## Contributing

Contributions are welcome! Please submit a pull request for any features or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
```
