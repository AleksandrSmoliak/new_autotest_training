from selenium.webdriver.firefox.webdriver import WebDriver
from fiture.session import SessionHelper
from fiture.group import GroupHelper
from fiture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    # Проверякм валидность сессии по наличию урла
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
