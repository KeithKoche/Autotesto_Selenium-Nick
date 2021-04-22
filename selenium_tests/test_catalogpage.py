import pytest
import allure

from cataloguepage import PageCatalogue




@allure.title("Открыта страница каталога товаров")
def test_cataloguepage_view(browse):
    catalogue_view = PageCatalogue(browse)
    catalogue_view.cataloguepage_open(browse)
    catalogue_view.cataloguepage_view()

@allure.title("Отображен список товаров")
def test_goodslist_is_present(browse):
    catalogue_view = PageCatalogue(browse)
    catalogue_view.cataloguepage_open(browse)
    catalogue_view.goodslist_is_present()