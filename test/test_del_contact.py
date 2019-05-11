from model.contact import Contact
import random


def test_del_contact(app, db):
    # Проверяем наличие контактов. Если их нет создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Смоляк"))
    # Получаем старый список контактов из БД
    old_contacts = db.get_contact_list()
    # Получаем случайный контакт из полученного списка контактов
    contact = random.choice(old_contacts)
    # Удаление случайного контакта по индексу
    app.contact.delete_contact_by_id(contact.id)
    # Получаем новый список контактов
    new_contacts = db.get_contact_list()
    # Сравниваем длину старого и нового списков
    assert len(old_contacts) - 1 == len(new_contacts)
    # Удаляем из старого списка контактов элемент полученный с использованием случайного индекса
    old_contacts.remove(contact)
    # Сравниваем старый и новый списка групп
    assert old_contacts == new_contacts
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
