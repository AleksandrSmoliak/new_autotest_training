# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Создание новой группы
    app.group.create(Group(name="group name", header="group header", footer="group footer"))
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что произошло добавление новой группы сравнивая их длину
    assert len(old_groups) + 1 == len(new_groups)
    # Возврат на страницу со списком групп
    app.session.return_home_page()


def test_empty_group(app):
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Создание новой группы
    app.group.create(Group(name="", header="", footer=""))
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что произошло добавление новой группы сравнивая их длину
    assert len(old_groups) + 1 == len(new_groups)
    # Возврат на страницу со списком групп
    app.session.return_home_page()
