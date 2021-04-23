import logging
from os import path, remove
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if path.isfile("./logs/users.log"):
    remove("./logs/users.log")

class PageUser:
    path = "/index.php?route=account/login"

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('Страница пользовательской авторизации')
        self.logger.setLevel(logging.INFO)

        logger_handler = logging.FileHandler('./logs/users.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    def userpage_open(self, browse):
        self.logger.info("Страница открыта")
        self.driver.get(browse.url + self.path)

    def user_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "account-login")))
        browse.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        browse.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        browse.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "list-group")))
        browse.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Login']")))