from model.contact import Contact
import random


def test_modify_contact_firstname(app, db):
    # Проверяем налисие контактов, если нет - создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Тест"))
    # Получаем старый список контактов
    old_contact = db.get_contact_list()
    # Получаем случайный объект из списка контактов
    contact = random.choice(old_contact)
    # оздаем объект для изменения контакта
    contact_data = Contact(firstname="Владимир2", lastname="Геннадьевич2")
    # Выбираем и модифицируем первый найденный контакт
    app.contact.modify_contact_by_id(contact_data, contact.id)
    # Получаем новый список контактов
    new_contact = db.get_contact_list()
    # Сравниваем длину списков до и после модификации
    assert len(old_contact) == len(new_contact)
    # Удаляем старое заначение из списка
    old_contact.remove(contact)
    # Добавляем в новый объект id случайного контакта
    contact_data.id = contact.id
    # Добавляем новый объект в список
    old_contact.append(contact_data)
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
