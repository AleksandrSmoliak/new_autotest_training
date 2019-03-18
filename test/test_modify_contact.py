from model.contact import Contact


def test_modify_contact_firstname(app):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    # Получаем старый список контактов
    old_contact = app.contact.get_contact_list()
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_first_contact(Contact(firstname="Владимир"))
    # Получаем новый список контактов
    new_contact = app.contact.get_contact_list()
    # Сравниваем длину списков до и после модификации
    assert len(old_contact) == len(new_contact)
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