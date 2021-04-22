from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageUser:
    path = "/index.php?route=account/login"

    def __init__(self, driver):
        self.driver = driver

    def userpage_open(self, browse):
        self.driver.get(browse.url + self.path)

    def user_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "account-login")))
        browse.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        browse.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        browse.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "list-group")))
        browse.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Login']")))