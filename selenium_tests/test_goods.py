from goodspage import PageGoods


def test_goodspage_view(browse):
    goods_view = PageGoods(browse)
    goods_view.goodspage_open(browse)
    goods_view.goodspage_view()