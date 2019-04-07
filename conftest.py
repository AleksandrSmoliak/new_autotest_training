from fixture.application import Application
import pytest
import json

fixture = None  # Задаем глобальную переменную для определения валидности фикстуры
target = None  # Задаем глабальную переменную для определения конфига

@pytest.fixture
def app(request):
    global fixture  # Объявление глобальной переменной фикстуры
    global target  # Объявление глобальной переменной конфига
    # Создаем переменную в которую передаем параметр с типом браузера
    browser = request.config.getoption("--browser")
    # Загружаем конфиг если ранее он не был загружен
    if target is None:
        # Читаем конфигурационный файл переданный в виде параметра (содержимое загруженного файла передаем в
        # переменную config_file). P.S. Что бы прочитался файл при запуске из среды разработки необходимо указать
        # в настройках проекта рабочую директорию (указать адрес этого проекта)
        with open(request.config.getoption("--target")) as config_file:
            # В переменную target передаем содержимое загруженного файла как json
            target = json.load(config_file)
    # Проверяем, если фикстуры нету или она не валидна, тогда создаем ее.
    if fixture is None or not fixture.is_valid():
        # Создаем фикстуру (объект типа Application). Для передачи параметра из файла используем переменную target
        fixture = Application(browser=browser, base_url=target['baseURL'])
    # Авторизуемся. Для передачи параметра из файла используем переменную target
    fixture.session.ensure_login(username=target['username'], password=target['password'])
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
    parser.addoption("--target", action="store", default="target.json")
