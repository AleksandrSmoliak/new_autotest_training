def test_test_add_contact(app):
    # Логин
    app.session.login(username="admin", password="secret")
    # Добавление нового контакта
    app.contact.delete_first_contact()
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
    #Логаут
    app.session.logout()