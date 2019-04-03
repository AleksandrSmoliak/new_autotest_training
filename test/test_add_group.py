# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string


# Генератор случайных тестовых данных
def random_string(prefix, maxlen):
    # Присваиваем переменной наборы различных символов + пробел
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # Возвращаем строку из склеенных символов. Список будет из случайных символов и случайной длинны с ограничением на
    # значение maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Формируем 2 массива с данными. Первый пустой, а второй генерируется случайными данными, при этом генерируется
# указанное количество раз, что позволяет создать нескольео наборов с данными.
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]


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
