# -*- coding: utf-8 -*-
from model.group import Group
from fiture.application import Application
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
    app.session.login(username="admin", password="secret")
    # Создание новой группы
    app.group.create(Group(name="group name", header="group header", footer="group footer"))
    # Логаут
    app.session.logout()


def test_empty_group(app):
    # Авторизация
    app.session.login(username="admin", password="secret")
    # Создание новой группы
    app.group.create(Group(name="", header="", footer=""))
    # Логаут
    app.session.logout()
