from model.contact import Contact
import re
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # Переход на страницу с контактами
        self.open_contact_page()
        # Нажатие на кнопку создания контакта
        wd.find_element_by_link_text("add new").click()
        # Заполнение формы
        self.fill_contact_form(contact)
        # Сохранение данных формы
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # Возврат на страницу с контактами
        self.open_contact_page()
        # Очищаем кэш списка контактов
        self.contact_cache = None

    # Заполнение формы
    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.company_address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax_phone)
        self.change_field_value("phone2", contact.sec_phone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value_selected(contact.birthday_selected)
        self.change_field_value_selected(contact.birthmont_selected)
        self.change_field_value("byear", contact.byear)

    # Мотод проверки на передачу НЕ пустого значения. Если имеется переданное значение то заполняем поле
    # иначе оставляем то, что было.
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_selected(self, value):
        wd = self.app.wd
        if value is not None:
            if value !="":
                if not wd.find_element_by_xpath(value).is_selected():
                    wd.find_element_by_xpath(value).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    # Удаление контакта по переданному индексу
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # Переход на страницу контактов
        self.open_contact_page()
        # Активировать чекбокс (первый с этим именем)
        wd.find_elements_by_name("selected[]")[index].click()
        # Клик по кнопке удаления
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # Подтверждеие удаления элемента в окне алерта
        wd.switch_to_alert().accept()
        # Очищаем кэш списка контактов
        self.contact_cache = None

    # Удаление контакта по переданному id
    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # Переход на страницу контактов
        self.open_contact_page()
        # Активировать чекбокс c переданным id
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # Клик по кнопке удаления
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # Подтверждеие удаления элемента в окне алерта
        wd.switch_to_alert().accept()
        time.sleep(1)
        # Очищаем кэш списка контактов
        self.contact_cache = None

    # Переход на страницу с контактами
    def open_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring"))) > 0:
            wd.find_element_by_link_text("home").click()

    # Ищет все созданные контакты и вычисляет их длину
    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_field):
        self.modify_contact_by_index(new_contact_field, 0)

    # Модификация первого контакта
    def modify_contact_by_index(self, new_contact_field, index):
        wd = self.app.wd
        # Переход на страницу с контактами
        self.open_contact_page()
        # Выбор первой группы в режиме редактирования
        self.open_contact_modify_by_index(index)
        # Заполнение формы
        self.fill_contact_form(new_contact_field)
        # Сохранение изменений
        time.sleep(5)
        wd.find_element_by_name("update").click()
        # Очищаем кэш списка контактов
        self.contact_cache = None

    # Модификация контакта по id
    def modify_contact_by_id(self, new_contact_field, id):
        wd = self.app.wd
        # Переход на страницу с контактами
        self.open_contact_page()
        # Выбор первой группы в режиме редактирования
        self.open_contact_modify_by_id(id)
        # Заполнение формы
        self.fill_contact_form(new_contact_field)
        # Сохранение изменений
        time.sleep(5)
        wd.find_element_by_name("update").click()
        # Очищаем кэш списка контактов
        self.contact_cache = None

    # Открытие контакта с переданным ид на редактирование
    def open_contact_modify_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("//input[@id='%s']/../../td[8]/a/img" % id).click()

    # Открытие контакта с переданным индексом на редактирование
    def open_contact_modify_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()


    # Открытие контакта с переданным индексом на просмотр
    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    # Кеширование списка контактов
    contact_cache = None

    # Получение списка контактов со страницы в приложении
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                id = element.find_element_by_xpath("td[1]/input").get_attribute("id")
                ln = element.find_element_by_xpath("td[2]").text
                fn = element.find_element_by_xpath("td[3]").text
                # Получаем содержимое ячейки с адресом
                addr = element.find_element_by_xpath("td[4]").text
                # Получаем содержимое ячейки с мейлами
                all_mails = element.find_element_by_xpath("td[5]").text
                # Получаем содержимое ячейки с телефонами
                all_phones = element.find_element_by_xpath("td[6]").text
                # Формируем объект
                self.contact_cache.append(Contact(id=id, firstname=fn, lastname=ln, company_address=addr,
                                                  all_mails_from_home_page=all_mails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    # Получение информации о контакте со страницы редактирования
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_modify_by_index(index)
        id = wd.find_element_by_xpath("//input[@name='id']").get_attribute("value")
        firstname = wd.find_element_by_xpath("//input[@name='firstname']").get_attribute("value")
        lastname = wd.find_element_by_xpath("//input[@name='lastname']").get_attribute("value")
        addr = wd.find_element_by_xpath("//textarea[@name='address']").text
        email = wd.find_element_by_xpath("//input[@name='email']").get_attribute("value")
        email2 = wd.find_element_by_xpath("//input[@name='email2']").get_attribute("value")
        email3 = wd.find_element_by_xpath("//input[@name='email3']").get_attribute("value")
        home_phone = wd.find_element_by_xpath("//input[@name='home']").get_attribute("value")
        mobile_phone = wd.find_element_by_xpath("//input[@name='mobile']").get_attribute("value")
        work_phone = wd.find_element_by_xpath("//input[@name='work']").get_attribute("value")
        sec_phone = wd.find_element_by_xpath("//input[@name='phone2']").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, company_address=addr, email=email, email2=email2,
                       email3=email3, home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone,
                       sec_phone=sec_phone)

    # Получение информации о номерах телефонов со страницы просмотра контактов
    def get_contact_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        # Присваиваем переменной значение из элемента (все телефоны)
        text = wd.find_element_by_id("content").text
        # Находим через регулярку значение в данных с перфиксом и извлекаеи значение грруппы (то что в скобках)
        # это значение будет искомый номер телефона
        home_phone = (re.search("H:(.*)", text).group(1))
        mobile_phone = re.search("M:(.*)", text).group(1)
        work_phone = re.search("W:(.*)", text).group(1)
        sec_phone = re.search("P:(.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, sec_phone=sec_phone)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()

