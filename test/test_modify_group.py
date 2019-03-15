from model.group import Group


def test_modify_group_name(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Модификация первой группы. Изменение имени.
    app.group.modify_first_group(Group(name="New group"))
    app.session.return_home_page()


def test_modify_group_header(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Модификация первой группы. Изменение хедера.
    app.group.modify_first_group(Group(header="New header"))
    app.session.return_home_page()