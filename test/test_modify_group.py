from model.group import Group

def test_modify_group_name(app):
    # Авторизация
    app.session.login(username="admin", password="secret")
    # Создание новой группы
    app.group.modify_first_group(Group(name="New group"))
    # Логаут
    app.session.logout()


def test_modify_group_header(app):
    # Авторизация
    app.session.login(username="admin", password="secret")
    # Создание новой группы
    app.group.modify_first_group(Group(header="New header"))
    # Логаут
    app.session.logout()