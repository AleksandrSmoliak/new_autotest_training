from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    # Получаем старый список контактов
    old_contact = app.contact.get_contact_list()
    # Генерируем случайный индекс для выбора случайного контакта для изменения
    index = randrange(len(old_contact))
    # Локальна переменная для хранения объекта изменяемого контакта
    contact = Contact(firstname="Владимир")
    # Сохраняем ид модифицируемого контакта
    contact.id = old_contact[index].id
    # Сохраняем фамилию модифицируемого контакта
    contact.lastname = old_contact[index].lastname
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_contact_by_index(contact, index)
    # Получаем новый список контактов
    new_contact = app.contact.get_contact_list()
    # Сравниваем длину списков до и после модификации
    assert len(old_contact) == len(new_contact)
    # Присваиваем первому контакту модифицируемое значение
    old_contact[index] = contact
    # Сравниваем новый список из приложения со старым в которы добавили контакт через код
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    # Вернуться на домашнюю страницу
    app.session.return_home_page()


#def test_modify_contact_middlename(app):
#    # Проверяем налисие контактов, если нет - создаем
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Тест"))
#    # Выбираем и модифицируем первый найденный контакт
#    app.contact.modify_first_contact(Contact(middlename="Владимирович"))
#    # Вернуться на домашнюю страницу
#    app.session.return_home_page()


def test_modify_contact_lastname(app):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    old_contact = app.contact.get_contact_list()
    contact = Contact(lastname="Путин")
    contact.id = old_contact[0].id
    contact.firstname = old_contact[0].firstname
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_first_contact(contact)
    new_contact = app.contact.get_contact_list()
    old_contact[0] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
