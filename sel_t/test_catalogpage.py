import pytest
import allure
from catalogue import PageCatalogue

@allure.title("Тест перехода к странице каталога товаров")
def test_cataloguepage_view(browse):
    catalogue_view = PageCatalogue(browse)
    catalogue_view.cataloguepage_open(browse)
    catalogue_view.cataloguepage_view()
    allure.dynamic.title('Страница каталога товаров открыта')

@allure.severity(allure.severity_level.CRITICAL)
def test_goodslist_is_present(browse):
    catalogue_view = PageCatalogue(browse)
    catalogue_view.cataloguepage_open(browse)
    catalogue_view.goodslist_is_present()
    allure.dynamic.title('Список товаров присутствует')