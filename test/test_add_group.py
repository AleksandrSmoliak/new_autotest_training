# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Локальная переменная для передачи параметра в создаваемую группу
    group = Group(name="group name", header="group header", footer="group footer")
    # Создание новой группы
    app.group.create(group)
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что произошло добавление новой группы сравнивая их длину
    assert len(old_groups) + 1 == len(new_groups)
    # Добавляем создаваемую в прилжении группу в старую гуппу для дальнейшего сравнения
    old_groups.append(group)
    # Сравниваем старую и новую группу по содержанию. Сортировка по ИД вычесляемой в функции. Функция используется
    # в качестве ключа.
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Возврат на страницу со списком групп
    app.session.return_home_page()


def test_empty_group(app):
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Локальная переменная для передачи параметра в создаваемую группу
    group = Group(name="", header="", footer="")
    # Создание новой группы
    app.group.create(group)
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что произошло добавление новой группы сравнивая их длину
    assert len(old_groups) + 1 == len(new_groups)
    # Добавляем создаваемую в прилжении группу в старую гуппу для дальнейшего сравнения
    old_groups.append(group)
    # Сравниваем старую и новую группу по содержанию. Сортировка по ИД вычесляемой в функции. Функция используется
    # в качестве ключа.
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Возврат на страницу со списком групп
    app.session.return_home_page()
