import pytest
from adminpage import PageAdmin



def test_adminpage_view(browse):
    admpage_view = PageAdmin(browse)
    admpage_view.admpage_open(browse)
    admpage_view.adm_view()


def test_authorize_admin(browse):
    admin_authorize = PageAdmin(browse)
    admin_authorize.admpage_open(browse)
    admin_authorize.admpage_nameinput()
    admin_authorize.admpage_passinput()
    admin_authorize.admpage_authconfirm()

def test_forgot(browse):
     admin_forgot = PageAdmin(browse)
     admin_forgot.admpage_open(browse)
     admin_forgot.to_forgot()






