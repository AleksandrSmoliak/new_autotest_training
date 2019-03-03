# -*- coding: utf-8 -*-
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    # Создаем фикстуру (объект типа Application)
    fixture = Application()
    # Разрушение фикстуры используя существующий метод заррушения фикстуры
    request.addfinalizer(fixture.destroy)
    # Возвращаем фиксуру
    return fixture



def test_add_group(app):
    # Авторизация
    app.login(username="admin", password="secret")
    # Создание новой группы
    app.create_group(Group(name="group name", header="group header", footer="group footer"))
    # Логаут
    app.logout()

def test_empty_group(app):
    # Авторизация
    app.login(username="admin", password="secret")
    # Создание новой группы
    app.create_group(Group(name="", header="", footer=""))
    # Логаут
    app.logout()