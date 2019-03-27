from model.group import Group
from random import randrange


def test_delete_some_group(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Получаем случайный индекс из длины списка групп
    index = randrange(len(old_groups))
    # Удаление новой группы
    app.group.delete_group_by_index(index)
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что произошло удаление новой группы сравнивая их длину
    assert len(old_groups) - 1 == len(new_groups)
    # Удаляем первый элемент из старого списка групп
    old_groups[index:index+1] = []
    # Проверяем получившиеся списки групп
    assert old_groups == new_groups
    # Возврат на страницу со списком групп
    app.session.return_home_page()
