# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_test_add_contact(app):
    # Получаем старый список контактов
    old_contact = app.contact.get_contact_list()
    # Локальня переменная для передачи параметров в создаваемый контакт
    contact = Contact(firstname="Александр", middlename="Смоляк", lastname="Владимирович", nickname="crucis", title="Заголовок", company_name="Имя компании",
                               company_address="адрес компании", home_phone="9119999999", mobile_phone="9119999991", work_phone="9119999992", fax_phone="9119999993", email="as@as.ru",
                               email2="as@as2.ru", email3="as@as3.ru", homepage="www.homepage.ru",
                               birthday_selected="//div[@id='content']/form/select[1]//option[12]",
                               birthmont_selected="//div[@id='content']/form/select[2]//option[7]", byear="1983",
                               home_address="Домашний адрес")
    # Добавление нового контакта
    app.contact.create(contact)
    # Получаем новый список контактов
    new_contact = app.contact.get_contact_list()
    # Сравниваем длину списков до и после добавления
    assert len(old_contact) + 1 == len(new_contact)
    # Добавляем в старый список контактов создаваемый в приложении контакт
    old_contact.append(contact)
    # Сортируем и сравниваем старый и новый списка контактов
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    # Вернуться на домашнюю страницу
    app.session.return_home_page()

