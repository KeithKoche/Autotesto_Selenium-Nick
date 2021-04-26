import pytest
import allure
from startin import PageMain


@allure.title("Тестируем открытие стартовой страницы приложения")
def test_mainpage(browse):
    main_view = PageMain(browse)
    main_view.mainpage_open(browse)
    main_view.mainpage_view()
    allure.dynamic.title('Стартовая страница открыта')