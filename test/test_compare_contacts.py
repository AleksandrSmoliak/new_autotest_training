from random import randrange
import re


# Тест сравнения данных случайного контакта с главной страницы с данными со страницы редактирования
def test_compare_contacts(app):
    # Генерируем случайный индекс из длины списка контактов на странице
    index = randrange(app.contact.count())
    # Получаем контакт с главной страницы по сгенерированному индексу
    contact_from_home_page = app.contact.get_contact_list()[index]
    # Получаем контакт со страницы редактирования по сгенерированному индексу
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    # Сравниваем полученные данные предварительно склеив полученные данные(при необходимости)
    # 1. Сравниваем имя, фамилию и адресс компании
    assert contact_from_home_page.id == contact_from_edit_page.id
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    # 2. Сравниваем мейлы со склейкой
    assert contact_from_home_page.all_mails_from_home_page == merge_mails_like_on_home_page(contact_from_edit_page)
    # 3. Сравниваем телефоны со склейкой
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# Очищает переданное значение от лишних символов
def clear(s):
    # Заменяет по указанному шаблону (что, на что, где)
    return re.sub("[() -]", "", s)


def merge_mails_like_on_home_page(contact):
    # Склеиваем значения из переданного объекта. Строки очищаем от лишних символов, фильтруем значений имеющих значение
    # None и отвильтровываем получившиеся значения от пустых строк.
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    # Склеиваем значения из переданного объекта. Строки очищаем от лишних символов, фильтруем значений имеющих значение
    # None и отвильтровываем получившиеся значения от пустых строк.
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.sec_phone]))))
