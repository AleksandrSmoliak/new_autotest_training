

def test_delete_first_group(app):
    # Авторизация
    app.session.login(username="admin", password="secret")
    # Создание новой группы
    app.group.delete_first_group()
    # Логаут
    app.session.logout()