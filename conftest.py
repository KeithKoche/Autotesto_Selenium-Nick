import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--browser", action="store", default="chrome", choices=["ie", "firefox", "chrome"])
    parser.addoption("--burl", action="store", default="https://demo.opencart.com/")


@pytest.fixture
def browse(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--burl")

    driver = "chrome"

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless: options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless: options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "ie":
        options = webdriver.IeOptions()
        if headless: options.headless = True
        driver = webdriver.Ie(options=options)

    if maximized:
        driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver




