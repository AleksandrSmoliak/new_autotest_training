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
        wd = self.app.wd
        # Переход на страницу контактов
        self.open_contact_page()
        # Активировать чекбокс (первый с этим именем)
        wd.find_element_by_name("selected[]").click()
        # Клик по кнопке удаления
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # Подтверждеие удаления элемента в окне алерта
        wd.switch_to_alert().accept()

    # Переход на страницу с контактами
    def open_contact_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("searchstring"))) > 0:
            wd.find_element_by_link_text("home").click()

    # Ищет все созданные контакты и вычисляет их длину
    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    # Модификация первого контакта
    def modify_first_contact(self, new_contact_field):
        wd = self.app.wd
        # Переход на страницу с контактами
        self.open_contact_page()
        # Выбор первой группы в режиме редактирования
        self.open_first_contact_modify()
        # Заполнение формы
        self.fill_contact_form(new_contact_field)
        # Сохранение изменений
        wd.find_element_by_name("update").click()

    # Открытие первого контакта на редактирование
    def open_first_contact_modify(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@title='Edit']").click()