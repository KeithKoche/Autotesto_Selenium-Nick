from cataloguepage import PageCatalogue



def test_cataloguepage_view(browse):
    catalogue_view = PageCatalogue(browse)
    catalogue_view.cataloguepage_open(browse)
    catalogue_view.cataloguepage_view()


def test_goodslist_is_present(browse):
    catalogue_view = PageCatalogue(browse)
    catalogue_view.cataloguepage_open(browse)
    catalogue_view.goodslist_is_present()