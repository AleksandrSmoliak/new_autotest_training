def test_test_add_contact(app):
    # Добавление нового контакта
    app.contact.delete_first_contact()
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
