# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


# Генератор случайных строковых данных
def random_string(prefix, maxlen):
    # Присваиваем переменной наборы различных символов + пробел
    symbols = string.ascii_letters + string.digits + " "
    # Возвращаем строку из склеенных символов. Список будет из случайных символов и случайной длинны с ограничением на
    # значение maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Формируем 2 массива с данными. Первый пустой, а второй генерируется случайными данными, при этом генерируется
# указанное количество раз, что позволяет создать нескольео наборов с данными.
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company_name="", company_address="",
            home_phone="", mobile_phone="", work_phone="", fax_phone="", sec_phone="", email="", email2="",
            email3="", homepage="", birthday_selected="", birthmont_selected="", byear="", home_address="")] + [
    Contact(firstname=random_string("firstname_", 10), middlename=random_string("middlename_", 10),
            lastname=random_string("lastname_", 10), nickname=random_string("nickname_", 10),
            title=random_string("title_", 10), company_name=random_string("company_name_", 10),
            company_address=random_string("company_address_", 10), home_phone=random_string("home_phone_", 10),
            mobile_phone=random_string(" mobile_phone_", 10), work_phone=random_string("work_phone_", 10),
            fax_phone=random_string("fax_phone_", 10), sec_phone=random_string("sec_phone_", 10),
            email=random_string("email_", 10), email2=random_string("email2_", 10), email3=random_string("email3_", 10),
            homepage=random_string("homepage_", 10), birthday_selected="//div[@id='content']/form/select[1]//option[12]",
            birthmont_selected="//div[@id='content']/form/select[2]//option[7]", byear="1983",
            home_address=random_string("home_address_", 10))
    for i in range(10)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contact):
    # Получаем старый список контактов
    old_contact = app.contact.get_contact_list()
    # Добавление нового контакта
    app.contact.create(contact)
    # Получаем новый список контактов
    new_contact = app.contact.get_contact_list()
    # Сравниваем длину списков до и после добавления
    assert len(old_contact) + 1 == app.contact.count()
    # Добавляем в старый список контактов создаваемый в приложении контакт
    old_contact.append(contact)
    # Сортируем и сравниваем старый и новый списка контактов
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
    # Вернуться на домашнюю страницу
    app.session.return_home_page()

