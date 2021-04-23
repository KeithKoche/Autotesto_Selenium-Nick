import logging
from os import path, remove
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if path.isfile("./logs/admin.log"):
    remove("./logs/admin.log")


class PageAdmin:
    path = "/admin/"


    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('Страница входа в административный аккаунт')
        self.logger.setLevel(logging.INFO)

        logger_handler = logging.FileHandler('./logs/admin.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)



    def admpage_open(self, browse):
        self.logger.info("Страница открыта")
        self.driver.get(browse.url + self.path)

    def adm_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "header-logo")))
        browse.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        browse.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        browse.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Forgotten Password")))
        browse.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()=' Login']")))


    def admpage_nameinput(self):
        self.logger.info("Введен логин".format("demo"))
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("demo")

    def admpage_passinput(self):
        self.logger.info("Введен пароль".format("demo"))
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("demo")

    def admpage_authconfirm(self):
        self.logger.info("Ввод логина и пароля подтврежден")
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        self.driver.find_element(By.XPATH, "//*[text()=' Login']").click()
        browse.wait.until(EC.presence_of_element_located((By.ID, "user-profile")))

    def to_forgot(self):
        self.logger.info("Открыта страница восстановления пароля ")
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        self.driver.find_element(By.LINK_TEXT, "Forgotten Password").click()
        browse.wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()=' Forgot Your Password?']")))






