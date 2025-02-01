import pytest
from selenium import webdriver
from pluggy import HookimplMarker
import os

hookimpl = HookimplMarker("pytest")

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser name to execute tests on"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    
    try:
        if browser_name == "chrome":
            ops = webdriver.ChromeOptions()
            ops.add_argument("--disable-notifications")
            driver = webdriver.Chrome(options=ops)

        elif browser_name == "safari":
            ops = webdriver.SafariOptions()
            ops.add_argument("--disable-notifications")
            driver = webdriver.Safari(options=ops)
        elif browser_name == "firefox":
            ops = webdriver.FirefoxOptions()
            ops.add_argument("--disable-notifications")
            driver = webdriver.Firefox(options=ops)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
    except Exception as e:
        pytest.fail(f"Failed to initialize browser: {e}")
    
    driver.implicitly_wait(20)
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

@hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Extends the PyTest Plugin to take and embed screenshot in HTML report whenever a test fails.
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extras", [])
    
    if report.when in ["setup", "call"]:
        xfail = hasattr(report, "wasxfail")
        if (report.failed and not xfail) or (report.skipped and xfail):
            driver = item.funcargs.get("setup")
            if driver:
                file_name = report.nodeid.replace("::", "_") + ".png"
                file_path = _capture_screenshot(driver, file_name)
                if file_path:
                    html = (
                        '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>' % file_path
                    )
                    extra.append(pytest_html.extras.html(html))
    report.extras = extra

def _capture_screenshot(driver, name):
    """Captures a screenshot and returns the file path."""
    screenshots_dir = "/Users/riyabakoria/OrganixmantraAPP/.pytest_cache/Screenshots"
    os.makedirs(screenshots_dir, exist_ok=True)
    file_path = os.path.join(screenshots_dir, name)
    
    try:
        driver.get_screenshot_as_file(file_path)
        return file_path
    except Exception as e:
        print(f"Failed to take screenshot: {e}")
        return None

def pytest_configure(config):
    if config.pluginmanager.hasplugin("html"):
        metadata = config.stash.setdefault("metadata", {})
        metadata['Project Name'] = 'ATF Automation'
        metadata['Module Name'] = 'P.P. Page'
        metadata['Tester'] = 'Vinay Bakoria'
        print("Metadata added:", metadata)


def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)