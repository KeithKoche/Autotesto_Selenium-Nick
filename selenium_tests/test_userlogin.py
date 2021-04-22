import pytest
import allure
from userpage import PageUser



@allure.title("Открыта страница для пользовательской авторизации")
def test_userpage_view(browse):
    userpage_view = PageUser(browse)
    userpage_view.userpage_open(browse)
    userpage_view.user_view()