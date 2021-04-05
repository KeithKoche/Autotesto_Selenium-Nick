from mainpage import PageMain


def test_mainweb(browse):
    mainweb_view = PageMain(browse)
    mainweb_view.mainpage_open(browse)
    mainweb_view.mainweb()


