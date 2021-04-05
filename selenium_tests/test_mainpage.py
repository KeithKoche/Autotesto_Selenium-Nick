import pytest
from mainpage import PageMain


def test_mainpage(browse):
    main_view = PageMain(browse)
    main_view.mainpage_open(browse)
    main_view.mainpage_view()