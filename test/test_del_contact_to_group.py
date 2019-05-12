import random
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact
dbs = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_del_to_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group1", header="Group1_Header", footer="Group1_Footer"))
    elif len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Александр", middlename="Владимирович", lastname="Смоляк", nickname="Crucis",
                               title="Новый контакт",
                               home_phone="+7(812)999-99-99", mobile_phone="+7(911)923-00-99", work_phone="+7(812)777-77-77",
                               email="crucis.spb@gmail.com", homepage="http://site.ru/",
                               home_address="Домашний адрес"))
    elif len(db.get_group_with_contact_list()) == 0:
        # Получаем список контактов из БД
        contacts_db = db.get_contact_list()
        # Получаем список групп из БД
        groups_db = db.get_group_list()
        # Выбираем случайный контакт из полученного списка
        contact = random.choice(contacts_db)
        # Выбираeм случайную группу из полученного списка
        group = random.choice(groups_db)
        # В браузере выбираем контакт по ИД
        app.contact.select_contact_by_id(contact.id)
        # В браузере из выпадающего списка выбираем группу по ИД и добавляем контакт в группу
        app.group.add_to_group_by_id(group.id)

    # Получаем ИД групп которыке содержат контакты
    groups_with_contact = db.get_group_with_contact_list()
    # Выбираeм случайную группу из полученного списка
    group_id = random.choice(groups_with_contact)
    # Получаем список контактов из выбранной группы
    contacts = dbs.get_contacts_in_group(Group(id=group_id.id))
    # Получаем случайный контакт из полученного списка
    contact = random.choice(contacts)
    # Удаляем случайный контакт из выбранной группы
    app.contact.remove_contact_from_group(group_id.id, contact.id)
    # Получаем список контактов из выбранной группы
    l = dbs.get_contacts_in_group(Group(id=group_id.id))
    # Находим удаляемый контакт в полученном списке
    for item in l:
        if item.id != contact.id:
            # Если контакт не найден тогда проверка прошла
            assert True
    print(contact.id)
