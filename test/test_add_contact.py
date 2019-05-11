# -*- coding: utf-8 -*-
from model.contact import Contact


def test_test_add_contact(app, db, json_contact):
    # Присваиваем набор данных из параметра переменной используемой далее в тесте.
    contact = json_contact
    # Получаем старый список контактов из БД
    old_contact = db.get_contact_list()
    # Добавление нового контакта
    app.contact.create(contact)
    # Получаем новый список контактов из БД
    new_contact = db.get_contact_list()
    # Сравниваем длину списков до и после добавления
    assert len(old_contact) + 1 == app.contact.count()
    # Добавляем в старый список контактов создаваемый в приложении контакт
    old_contact.append(contact)
    # Сортируем и сравниваем старый и новый списка контактов
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    # Вернуться на домашнюю страницу
    app.session.return_home_page()

