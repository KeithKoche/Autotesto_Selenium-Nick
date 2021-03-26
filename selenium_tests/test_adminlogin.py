import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_adminlogin(browse):
    browse.get(browse.url + "/admin/")
    wait = WebDriverWait(browse, 3, 1)
    wait.until(EC.presence_of_element_located((By.ID, "header-logo")))
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Forgotten Password")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()=' Login']")))

def test_auth(browse):
    browse.get(browse.url + "/admin/")
    wait = WebDriverWait(browse, 3, 1)
    browse.find_element(By.NAME, "username").clear()
    browse.find_element(By.NAME, "password").clear()
    browse.find_element(By.NAME, "username").send_keys("demo")
    browse.find_element(By.NAME, "password").send_keys("demo")
    browse.find_element(By.XPATH, "//*[text()=' Login']").click()
    wait.until(EC.presence_of_element_located((By.ID, "user-profile")))
    assert browse.find_element(By.ID, "user-profile")


def test_forgot(browse):
    browse.get(browse.url + "/admin/")
    wait = WebDriverWait(browse, 3, 1)
    browse.find_element(By.LINK_TEXT, "Forgotten Password").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()=' Forgot Your Password?']")))
    assert browse.find_element(By.XPATH, "//*[text()=' Forgot Your Password?']")

