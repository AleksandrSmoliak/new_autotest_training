from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_link_text("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        # Переход на страницу с группами
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # Сохранение данных формы
        wd.find_element_by_name("submit").click()
        # Возврат на страницу со списком групп
        self.return_to_group_page()

# Заполнение формы
    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

# Мотод проверки на передачу НЕ пустого значения. Если имеется переданное значение то заполняем поле
# иначе оставляем то, что было.
    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        # Переход на страницу с группами
        self.open_group_page()
        # Выбор первой группы
        self.select_first_group()
        # Удаление первой группы
        wd.find_element_by_name("delete").click()
        # Возврат на страницу со списком групп
        self.return_to_group_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

# Модификация первой группы
    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        # Переход на страницу с группами
        self.open_group_page()
        # Выбор первой группы
        self.select_first_group()
        # Откртие формы для модификации
        wd.find_element_by_name("edit").click()
        # Заполение формы
        self.fill_group_form(new_group_data)
        # Подтверждение изменений
        wd.find_element_by_name("update").click()
        # Возврат на страницу со списком групп
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.app.wd
        # Проверяем находимся ли мы на данной странице. Если да, то переход не делаем
        if not(wd.current_url.endswith("/group.php") and len(wd.find_elements_by_link_text("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    # Считаем количество элементов с указанным именем
    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    # Получение списка групп
    def get_group_list(self):
        wd = self.app.wd
        self.open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector('span.group'):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups
