# -*- coding: utf-8 -*-
from model.group import Group
import pytest
# Импортируем генератор тестовых данных из файла (созданный пакет для хранения тестовых данных)
#from data.add_group import testdata
# При необходимости использовать другой набор данных из файла, что бы не переписывать код теста
from data.groups import constant as testdata


# Первая строка говорит, что тест парамметризован и указываем что передеаем и откуда в качестве данных
# в параметре ids передается представление тестовых данных
#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
# В тесте во втором параметре указываем на источник тестовых данных который подтягивается из
# фикстуры (pytest_generate_tests)
def test_add_group(app, db, json_group):
    # Присваиваем набор данных из параметра переменной используемой далее в тесте.
    group = json_group
    # Получаем старый список групп из БД
    old_groups = db.get_group_list()
    # Создание новой группы из приложения
    app.group.create(group)
    # Получаем новый список групп из БД
    new_groups = db.get_group_list()
    # Добавляем создаваемую в прилжении группу в старую гуппу для дальнейшего сравнения
    old_groups.append(group)
    # Сравниваем старую и новую группу по содержанию. Сортировка по ИД вычесляемой в функции. Функция используется
    # в качестве ключа.
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Возврат на страницу со списком групп
    app.session.return_home_page()
