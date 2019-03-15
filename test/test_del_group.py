from model.group import Group


def test_delete_first_group(app):
    # Проверяем наличие групп. Если их нет, то создаем.
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    # Удаление новой группы
    app.group.delete_first_group()
    app.session.return_home_page()
