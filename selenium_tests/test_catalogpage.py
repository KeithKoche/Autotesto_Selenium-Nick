import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_cataloguepage(browse):
    browse.get(browse.url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browse, 3, 1)
    wait.until(EC.visibility_of_element_located((By.ID, "menu")))
    wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-header")))
    wait.until(EC.visibility_of_element_located((By.ID, "compare-total")))
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))


def test_goodslist_is_present(browse):
    browse.get(browse.url + "/index.php?route=product/category&path=20")
    wait = WebDriverWait(browse, 3, 1)
    wait.until(EC.presence_of_element_located((By.ID, "content")))
    assert browse.find_element(By.ID, "content")
