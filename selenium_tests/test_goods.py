import pytest
import allure

from goodspage import PageGoods



@allure.title("Открыта страница едничным товаром")
def test_goodspage_view(browse):
    goods_view = PageGoods(browse)
    goods_view.goodspage_open(browse)
    goods_view.goodspage_view()