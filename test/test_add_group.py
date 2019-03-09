# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Создание новой группы
    app.group.create(Group(name="group name", header="group header", footer="group footer"))


def test_empty_group(app):
    # Создание новой группы
    app.group.create(Group(name="", header="", footer=""))
