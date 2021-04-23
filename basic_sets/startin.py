import logging
from os import path, remove
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if path.isfile("./logs/main.log"):
    remove("./logs/main.log")

class PageMain:


    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('Стартовая страница')
        self.logger.setLevel(logging.INFO)

        logger_handler = logging.FileHandler('./logs/main.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    def mainpage_open(self, browse):
        self.logger.info("Страница открыта")
        self.driver.get(browse.url)

    def mainweb(self):
        self.logger.info("ЮРЛ тот самый")
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3)
        browse.wait.until(EC.url_to_be("https://demo.opencart.com/"))

    def mainpage_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.visibility_of_element_located((By.ID, "slideshow0")))
        browse.wait.until(EC.visibility_of_element_located((By.NAME, "search")))
        browse.wait.until(EC.visibility_of_element_located((By.ID, "cart")))
        browse.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swiper-pager")))
        browse.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Featured']")))