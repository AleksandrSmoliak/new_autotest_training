# Тест сравнения контактов на главной странице и странице редактирования
def test_phones_on_home_page(app):
    # Получаем контакт с указанным индексом с главной страницы
    contact_from_home_page = app.contact.get_contact_list()[0]
    # Получаем свойства контакта с указанным индексом со страницы редактирования
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    # Сравниваем значения полей с главной страницы и со страницы редактирования контакта
    assert contact_from_home_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_home_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_home_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_home_page.sec_phone == contact_from_edit_page.sec_phone
