import pytest
import allure
from mainpage import PageMain



@allure.severity(allure.severity_level.TRIVIAL)
def test_mainweb(browse):
    mainweb_view = PageMain(browse)
    mainweb_view.mainpage_open(browse)
    mainweb_view.mainweb()


