from model.group import Group
from random import randrange

def test_modify_group_name(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Вычисляем случайный индекс модифицируемой группы и длинны списка групп
    index = randrange(len(old_groups))
    # Создаем локальную переменную для передачи в не объекта модифицируемой группы
    group = Group(name="New group")
    # Сохраняем ид модифицируемой группы из старого списка  и присваиваем его первому элементу списка который будем
    # добавлять для сравнения. Нужно для сравнения. т.к. ид измениться не должен.
    group.id = old_groups[index].id
    # Модификация первой группы. Изменение имени.
    app.group.modify_group_by_index(group, index)
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что длина предыдущего списка групп равнасписку групп после изменения
    assert len(old_groups) == len(new_groups)
    # Присваиваем первому элементу списка с которым будем сравнивать, сохраненный ранее элемент с полученным из него ид.
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    # Возврат на страницу со списком групп
    app.session.return_home_page()


def test_modify_group_header(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Модификация первой группы. Изменение хедера.
    app.group.modify_first_group(Group(header="New header"))
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что длина предыдущего списка групп равнасписку групп после изменения
    assert len(old_groups) == len(new_groups)
    # Возврат на страницу со списком групп
    app.session.return_home_page()
