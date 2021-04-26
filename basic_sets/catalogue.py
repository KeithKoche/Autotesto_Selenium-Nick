import logging
from os import path, remove
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if path.isfile("./logs/catalogue.log"):
    remove("./logs/catalogue.log")

class PageCatalogue:
    path = "/index.php?route=product/category&path=20"


    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('Страница каталога товаров')
        self.logger.setLevel(logging.INFO)

        logger_handler = logging.FileHandler('./logs/catalogue.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    def cataloguepage_open(self, browse):
        self.logger.info("Страница открыта")
        self.driver.get(browse.url + self.path)

    def cataloguepage_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.visibility_of_element_located((By.ID, "menu")))
        browse.wait.until(EC.visibility_of_element_located((By.NAME, "search")))
        browse.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-header")))
        browse.wait.until(EC.visibility_of_element_located((By.ID, "compare-total")))
        browse.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Desktops")))

    def goodslist_is_present(self):
        self.logger.info("Список товаров присутствует")
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "content")))
