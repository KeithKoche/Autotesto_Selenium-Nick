import pytest
import allure
from aacount import PageAdmin

@allure.title("Тест перехода к странице аминистративной авторизации")
def test_adminpage_view(browse):
    admpage_view = PageAdmin(browse)
    admpage_view.admpage_open(browse)
    admpage_view.adm_view()
    allure.dynamic.title('Страница административной авторизации открыта')

@allure.description("Тест на авторизацию в аккаунте администратора. Вероятно данная возможность забагована ")
def test_authorize_admin(browse):
    admin_authorize = PageAdmin(browse)
    admin_authorize.admpage_open(browse)
    admin_authorize.admpage_nameinput()
    admin_authorize.admpage_passinput()
    admin_authorize.admpage_authconfirm()
    allure.dynamic.title('Валидации логина и пароля нет. Принимаются любые значения')

@allure.title("Переход на страницу восстановления пароля")
def test_forgot(browse):
    admin_forgot = PageAdmin(browse)
    admin_forgot.admpage_open(browse)
    admin_forgot.to_forgot()
    allure.dynamic.title('Страница восстановления пароля открыта')






