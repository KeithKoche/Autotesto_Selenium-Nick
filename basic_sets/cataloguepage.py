from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageCatalogue:
    path = "/index.php?route=product/category&path=20"


    def __init__(self, driver):
        self.driver = driver

    def cataloguepage_open(self, browse):
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
        browse = self.driver
        browse.wait = WebDriverWait(browse, 3, 1)
        browse.wait.until(EC.presence_of_element_located((By.ID, "content")))
