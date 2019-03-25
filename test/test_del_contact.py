from model.contact import Contact
from random import randrange

def test_del_contact(app):
    # Проверяем наличие контактов. Если их нет создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Смоляк"))
    # Получаем старый список контактов
    old_contacts = app.contact.get_contact_list()
    # Генерируем случайный индекс для выбора случайной группы из списка
    index = randrange(len(old_contacts))
    # Удаление случайного контакта по индексу
    app.contact.delete_contact_by_index(index)
    # Получаем новый список контактов
    new_contacts = app.contact.get_contact_list()
    # Сравниваем длину старого и нового списков
    assert len(old_contacts) - 1 == len(new_contacts)
    # Удаляем из старого списка контактов элемент полученный с использованием случайного индекса
    old_contacts[index:index + 1] = []
    # Сравниваем старый и новый списка групп
    assert old_contacts == new_contacts
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
