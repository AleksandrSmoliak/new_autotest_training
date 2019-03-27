from model.contact import Contact


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

    # Переход на страницу с контактами
    def open_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring"))) > 0:
            wd.find_element_by_link_text("home").click()

    # Ищет все созданные контакты и вычисляет их длину
    def count(self):
        wd = self.app.wd
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
        wd.find_element_by_name("update").click()
        # Очищаем кэш списка контактов
        self.contact_cache = None

    # Открытие первого контакта на редактирование
    def open_contact_modify_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

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
                # Получаем содержимое ячейки с телефонами и разделяем его по переводу строки
                all_phones = element.find_element_by_xpath("td[6]").text.splitlines()
                # Формируем объект
                self.contact_cache.append(Contact(id=id, lastname=ln, firstname=fn, home_phone=all_phones[0],
                                                  mobile_phone=all_phones[1], work_phone=all_phones[2],
                                                  sec_phone=all_phones[3]))
        return list(self.contact_cache)

    # Получение информации о контакте со страницы редактирования
    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_modify_by_index(index)
        id = wd.find_element_by_xpath("//input[@name='id']").get_attribute("value")
        firstname = wd.find_element_by_xpath("//input[@name='firstname']").get_attribute("value")
        lastname = wd.find_element_by_xpath("//input[@name='lastname']").get_attribute("value")
        home_phone = wd.find_element_by_xpath("//input[@name='home']").get_attribute("value")
        mobile_phone = wd.find_element_by_xpath("//input[@name='mobile']").get_attribute("value")
        work_phone = wd.find_element_by_xpath("//input[@name='work']").get_attribute("value")
        sec_phone = wd.find_element_by_xpath("//input[@name='phone2']").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, sec_phone=sec_phone)
