class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    # Проверяем, что мы разлогинены
    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    # Проверка на наличие ссылки логаута. Нужно для проверки являемся ли мы авторизованными или нет.
    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    # Проверка на то, что мы авторизованы под нужным юзером.
    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div/div[1]/form/b").text == "("+username+")"

    # Проверяем, что мы залогинены
    def ensure_login(self, username, password):
        if self.is_logged_in():
            # Проверяем, что авторизованы под нужным юзером
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

