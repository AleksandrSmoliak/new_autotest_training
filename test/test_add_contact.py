# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_test_add_contact(app):
    # Логин
    app.session.login(username="admin", password="secret")
    # Добавление нового контакта
    app.contact.add_new_contact(Contact(firstname="Александр", middlename="Смоляк", lastname="Владимирович", nickname="crucis", title="Заголовок", company_name="Имя компании",
                          company_address="адрес компании", home_phone="9119999999", mobile_phone="9119999991", work_phone="9119999992", fax_phone="9119999993", email="as@as.ru",
                          email2="as@as2.ru", email3="as@as3.ru", homepage="www.homepage.ru",
                          birthday_selected="//div[@id='content']/form/select[1]//option[12]",
                          birthmont_selected="//div[@id='content']/form/select[2]//option[7]", byear="1983"))
    # Вернуться на домашнюю страницу
    app.session.return_home_page()
    #Логаут
    app.session.logout()

