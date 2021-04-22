import pytest
import allure
from adminpage import PageAdmin


@allure.title("Открыта страница административной авторизации")
def test_adminpage_view(browse):
    admpage_view = PageAdmin(browse)
    admpage_view.admpage_open(browse)
    admpage_view.adm_view()

@allure.title("Запущена авторизация администратора")
def test_authorize_admin(browse):
    admin_authorize = PageAdmin(browse)
    admin_authorize.admpage_open(browse)
    admin_authorize.admpage_nameinput()
    admin_authorize.admpage_passinput()
    admin_authorize.admpage_authconfirm()

    @allure.title("Переход к окну восстановления пароля")
    def test_forgot(browse):
        admin_forgot = PageAdmin(browse)
        admin_forgot.admpage_open(browse)
        admin_forgot.to_forgot()






