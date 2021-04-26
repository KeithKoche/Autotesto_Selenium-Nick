import pytest
import allure
from users import PageUser

@allure.title("Тест на переход к странице пользовательской авторизации")
def test_userpage_view(browse):
    userpage_view = PageUser(browse)
    userpage_view.userpage_open(browse)
    userpage_view.user_view()
    allure.dynamic.title('Страница пользовательской авторизации открыта')