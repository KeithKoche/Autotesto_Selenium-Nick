from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageGoods:
    path = "/index.php?route=product/product&path=57&product_id=49"


    def __init__(self, driver):
        self.driver = driver

    def goodspage_open(self, browse):
        self.driver.get(browse.url + self.path)

    def goodspage_view(self):
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "product")))
        browse.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Write a review")))
        browse.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))
        browse.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image-additional")))
        browse.wait.until(EC.visibility_of_element_located((By.NAME, "quantity")))