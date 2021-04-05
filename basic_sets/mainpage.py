from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageMain:


    def __init__(self, driver):
        self.driver = driver

    def mainpage_open(self, browse):
        self.driver.get(browse.url)

    def mainweb(self):
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