# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_group(self):
        wd = self.wd
        # Пререход на домашнюю страницу
        self.open_home_page(wd)
        # Авторизация
        self.login(wd, username="admin", password="secret")
        # Переход на страницу с группами
        self.open_group_page(wd)
        # Создание новой группы
        self.create_group(wd, name="group name", header="group header", footer="group footer")
        # Возврат на страницу со списком групп
        self.return_to_group_page(wd)
        # Логаут
        self.logout(wd)

    def test_empty_group(self):
        wd = self.wd
        # Пререход на домашнюю страницу
        self.open_home_page(wd)
        # Авторизация
        self.login(wd, username="admin", password="secret")
        # Переход на страницу с группами
        self.open_group_page(wd)
        # Создание новой группы
        self.create_group(wd, name="", header="", footer="")
        # Возврат на страницу со списком групп
        self.return_to_group_page(wd)
        # Логаут
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd, name, header, footer):
        wd.find_element_by_name("new").click()
        # Заполнение формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # Сохранение данных формы
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
