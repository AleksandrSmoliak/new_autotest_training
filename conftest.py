from fixture.application import Application
import pytest

fixture = None  # Задаем глобальную переменную для определения валидности фикстуры


@pytest.fixture
def app(request):
    global fixture  # Объявление глобальной переменной
    # Создаем переменную в которую передаем параметр с типом браузера
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseURL")
    # Проверяем, если фикстуры нету или она не валидна, тогда создаем ее.
    if fixture is None:
        # Создаем фикстуру (объект типа Application)
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            # Создаем фикстуру (объект типа Application)
            fixture = Application(browser=browser, base_url=base_url)
            # Авторизация
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


# Разрушение фикстуры используя существующий метод разрушения фикстуры, а перед этим делаем логаут из системы
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    # Возвращаем фиксуру
    return fixture


# Функция позволяющая через параметр в консоли передавать тип браузера
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
