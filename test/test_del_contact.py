from model.contact import Contact


def test_del_contact(app):
    # Проверяем наличие контактов. Если их нет создаем
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Смоляк"))
    # Добавление нового контакта
    app.contact.delete_first_contact()
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
