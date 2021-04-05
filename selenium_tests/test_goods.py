from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_goodspage(browse):
    browse.get(browse.url + "/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browse, 3, 1)
    wait.until(EC.presence_of_element_located((By.ID, "product")))
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Write a review")))
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='button-cart']")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image-additional")))
    wait.until(EC.visibility_of_element_located((By.NAME, "quantity")))