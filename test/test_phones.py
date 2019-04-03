import re


# Тест сравнения контактов на главной странице и странице редактирования
def test_phones_on_home_page(app):
    # Получаем контакт с указанным индексом с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[0]
    # Получаем свойства контакта с указанным индексом со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравниваем значения полей с главной страницы и со страницы редактирования контакта
    # Проверяемые значения очищаем от лишних символов
    debug = merge_phones_like_on_home_page(contact_from_edit_page)
    debug1 = contact_from_home_page.all_phones_from_home_page
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


# Тест сравнения телефонов со страницы просмотра контактов c контактами со страницы редактирования
def test_phones_on_contact_view_page(app):
    # Получаем контакт с указанным индексом с главной страницы
    contact_from_view_page = app.contact.get_contact_view_page(0)
    # Получаем свойства контакта с указанным индексом со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравниваем значения полей с главной страницы и со страницы просмотра контакта
    assert clear_space(contact_from_view_page.home_phone) == contact_from_edit_page.home_phone
    assert clear_space(contact_from_view_page.mobile_phone) == contact_from_edit_page.mobile_phone
    assert clear_space(contact_from_view_page.work_phone) == contact_from_edit_page.work_phone
    assert clear_space(contact_from_view_page.sec_phone) == contact_from_edit_page.sec_phone


# Очищаем строку от лишних паробелов
def clear_space(s):
    return s.strip()


# Очищает переданное значение от лишних символов
def clear(s):
    # Заменяет по указанному шаблону (что, на что, где)
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    # Склеиваем значения из переданного объекта. Строки очищаем от лишних символов, фильтруем значений имеющих значение
    # None и отвильтровываем получившиеся значения от пустых строк.
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone,
                                        contact.sec_phone]))))


