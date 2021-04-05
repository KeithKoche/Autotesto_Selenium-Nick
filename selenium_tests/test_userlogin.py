import pytest
from userpage import PageUser

def test_userpage_view(browse):
    userpage_view = PageUser(browse)
    userpage_view.userpage_open(browse)
    userpage_view.user_view()