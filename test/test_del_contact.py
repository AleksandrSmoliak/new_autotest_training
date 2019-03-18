from model.contact import Contact


def test_del_contact(app):
    # Проверяем наличие контактов. Если их нет создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Смоляк"))
    # Получаем старый список контактов
    old_contacts = app.contact.get_contact_list()
    # Удаление первого контакта
    app.contact.delete_first_contact()
    # Получаем новый список контактов
    new_contacts = app.contact.get_contact_list()
    # Сравниваем длину старого и нового списков
    assert len(old_contacts) - 1 == len(new_contacts)
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
