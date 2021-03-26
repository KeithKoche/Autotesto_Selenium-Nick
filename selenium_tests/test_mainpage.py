import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mainpage(browse):
    browse.get(browse.url)
    wait = WebDriverWait(browse, 3, 1)
    wait.until(EC.visibility_of_element_located((By.ID, "slideshow0")))
    wait.until(EC.visibility_of_element_located((By.NAME, "search")))
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swiper-pager")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Featured']")))