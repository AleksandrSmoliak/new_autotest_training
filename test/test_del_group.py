from model.group import Group


def test_delete_first_group(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Удаление новой группы
    app.group.delete_first_group()
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что произошло удаление новой группы сравнивая их длину
    assert len(old_groups) - 1 == len(new_groups)
    # Удаляем первый элемент из старого списка групп
    old_groups[0:1] = []
    # Проверяем получившиеся списки групп
    assert old_groups == new_groups
    # Возврат на страницу со списком групп
    app.session.return_home_page()
