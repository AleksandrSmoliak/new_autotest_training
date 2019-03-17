from model.group import Group


def test_modify_group_name(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Получаем старый список групп
    old_groups = app.group.get_group_list()
    # Модификация первой группы. Изменение имени.
    app.group.modify_first_group(Group(name="New group"))
    # Получаем новый список групп
    new_groups = app.group.get_group_list()
    # Проверяем что длина предыдущего списка групп равнасписку групп после изменения
    assert len(old_groups) == len(new_groups)
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
