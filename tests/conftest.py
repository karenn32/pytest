import pytest
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption(
        "--test-browser",  # Changed from --browser to --test-browser
        action="store", 
        default="firefox", 
        help="Choose a browser: firefox, chrome, or webkit"
    )

@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--test-browser")  # Use the new option
    with sync_playwright() as p:
        if browser_name == "firefox":
            browser = p.firefox.launch(headless=True)  # Use `headless=True` for headless mode
        elif browser_name == "chrome":
            browser = p.chromium.launch(headless=True)  # Launch Chromium (Chrome)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)  # Launch WebKit (Safari)
        else:
            raise ValueError(f"Unknown browser: {browser_name}")

        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()
