# -*- coding: utf-8 -*-
from model.group import Group
import pytest
# Импортируем генератор тестовых данных из файла (созданный пакет для хранения тестовых данных)
#from data.add_group import testdata
# При необходимости использовать другой набор данных из файла, что бы не переписывать код теста
from data.add_group import constant as testdata


# Первая строка говорит, что тест парамметризован и указываем что передеаем и откуда в качестве данных
# в параметре ids передается представление тестовых данных
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Создание новой группы
    app.group.create(group)
    # Проверяем что произошло добавление новой группы сравнивая их длину.
    # Сравниваем с хешем получая длину списка функцией
    assert len(old_groups) + 1 == app.group.count()
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Добавляем создаваемую в прилжении группу в старую гуппу для дальнейшего сравнения
    old_groups.append(group)
    # Сравниваем старую и новую группу по содержанию. Сортировка по ИД вычесляемой в функции. Функция используется
    # в качестве ключа.
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Возврат на страницу со списком групп
    app.session.return_home_page()
