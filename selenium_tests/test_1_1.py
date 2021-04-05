import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mainweb(browse):
    browse.get(browse.url)
    wait = WebDriverWait(browse, 3)
    wait.until(EC.url_to_be("https://demo.opencart.com/"))
    assert browse.current_url == "https://demo.opencart.com/"


