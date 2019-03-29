import re


# Тест сравнения контактов на главной странице и странице редактирования
def test_phones_on_home_page(app):
    # Получаем контакт с указанным индексом с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[0]
    # Получаем свойства контакта с указанным индексом со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравниваем значения полей с главной страницы и со страницы редактирования контакта
    # Проверяемые значения очищаем от лишних символов
    assert contact_from_home_page.home_phone == clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.mobile_phone == clear(contact_from_edit_page.mobile_phone)
    assert contact_from_home_page.work_phone == clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.sec_phone == clear(contact_from_edit_page.sec_phone)


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

