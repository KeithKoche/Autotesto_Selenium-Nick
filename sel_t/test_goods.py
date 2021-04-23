import pytest
import allure
from goods import PageGoods


@allure.severity(allure.severity_level.CRITICAL)
def test_goodspage_view(browse):
    goods_view = PageGoods(browse)
    goods_view.goodspage_open(browse)
    goods_view.goodspage_view()
    allure.dynamic.title('Страница товара открыта')