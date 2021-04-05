import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--maxres", action="store_true")
    parser.addoption("--head", action="store_true")
    parser.addoption("--bwr", action="store", default="chrome", choices=["ie", "firefox", "chrome"])
    parser.addoption("--burl", action="store", default="https://demo.opencart.com/")



@pytest.fixture
def browse(request):
    browser = request.config.getoption("--bwr")
    headless = request.config.getoption("--head")
    maximized = request.config.getoption("--maxres")
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






