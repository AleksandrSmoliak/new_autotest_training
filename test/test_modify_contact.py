from model.contact import Contact


def test_modify_contact_firstname(app):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_first_contact(Contact(firstname="Владимир"))
    # Вернуться на домашнюю страницу
    app.session.return_home_page()


def test_modify_contact_middlename(app):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_first_contact(Contact(middlename="Владимирович"))
    # Вернуться на домашнюю страницу
    app.session.return_home_page()


def test_modify_contact_lastname(app):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_first_contact(Contact(lastname="Путин"))
    # Вернуться на домашнюю страницу
    app.session.return_home_page()




