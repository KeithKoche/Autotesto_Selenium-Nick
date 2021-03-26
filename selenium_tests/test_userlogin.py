from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_userlogin(browse):
    browse.get(browse.url + "/index.php?route=account/login")
    wait = WebDriverWait(browse, 3, 1)
    wait.until(EC.presence_of_element_located((By.ID, "account-login")))
    wait.until(EC.presence_of_element_located((By.NAME, "email")))
    wait.until(EC.presence_of_element_located((By.NAME, "password")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "list-group")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Login']")))