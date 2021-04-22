import pytest
import allure
from mainpage import PageMain




@allure.title("Открыта главная страница")
def test_mainpage(browse):
    main_view = PageMain(browse)
    main_view.mainpage_open(browse)
    main_view.mainpage_view()