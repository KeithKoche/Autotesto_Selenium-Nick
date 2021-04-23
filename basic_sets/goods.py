import logging
from os import path, remove
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if path.isfile("./logs/goods.log"):
    remove("./logs/goods.log")

class PageGoods:
    path = "/index.php?route=product/product&path=57&product_id=49"


    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger('Страница товара')
        self.logger.setLevel(logging.INFO)

        logger_handler = logging.FileHandler('./logs/goods.log')
        logger_handler.setLevel(logging.INFO)
        logger_formatter = logging.Formatter('%(asctime)s- %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    def goodspage_open(self, browse):
        self.logger.info("Страница открыта")
        self.driver.get(browse.url + self.path)

    def goodspage_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "product")))
        browse.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Write a review")))
        browse.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))
        browse.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image-additional")))
        browse.wait.until(EC.visibility_of_element_located((By.NAME, "quantity")))