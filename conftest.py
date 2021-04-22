import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--bwr", action="store", default="chrome")
    parser.addoption("--burl", action="store", default="https://demo.opencart.com/")
    parser.addoption("--xcr", action="store", default="192.168.1.48")
    parser.addoption("--brover", action="store", default="89.0")
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=True)

@pytest.fixture
def browse(request):
    browser = request.config.getoption("--bwr")
    url = request.config.getoption("--burl")
    executor = request.config.getoption("--xcr")
    version = request.config.getoption("--brover")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")

    executor_url = f"http://{executor}:4444/wd/hub"

    capabilities = {
        "browserName": browser,
        "browserVersion": version,
        "screenResolution": "1600x900",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableLog": logs
        }
        }

    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities
    )

    request.addfinalizer(driver.close)
    driver.get(url)
    driver.url = url
    return driver






