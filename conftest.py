from fixture.application import Application
import pytest
import jsonpickle
import os.path
import importlib
import json
from fixture.db import DbFixture

fixture = None  # Задаем глобальную переменную для определения валидности фикстуры
target = None  # Задаем глабальную переменную для определения конфига


# Инициализируем отдельную функцию, которая будет заниматься загрузкой данных из файла
def load_config(file):
    global target # Объявление глобальной переменной конфига
    if target is None:
        # Определяем местоположение конфига относительно текущего файла и присваиваем его переременной
        # которую далее используем для чтения содержимого конфига
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        # Читаем конфигурационный файл переданный в виде параметра (содержимое загруженного файла передаем в
        # переменную f).
        with open(config_file) as f:
            # В переменную target передаем содержимое загруженного файла как json
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture  # Объявление глобальной переменной фикстуры
    # Создаем переменную в которую передаем параметр с типом браузера
    browser = request.config.getoption("--browser")
    # Загружаем данные из конфига из блока web
    web_config = load_config(request.config.getoption("--target"))['web']
    # Проверяем, если фикстуры нету или она не валидна, тогда создаем ее.
    if fixture is None or not fixture.is_valid():
        # Создаем фикстуру (объект типа Application). Для передачи параметра из файла используем переменную target
        fixture = Application(browser=browser, base_url=web_config['baseURL'])
    # Авторизуемся. Для передачи параметра из файла используем переменную target
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
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


# Функция определяющая необходимость выполнения проверок из пользовательского интерфейса
@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


# Функция позволяющая через параметр в консоли передавать тип браузера
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    # store_true - при таком значении автоматически указывается true если опция присутствует и false если отсутствует
    parser.addoption("--check_ui", action="store_true")




# Предназначено для определения переменной в тестах которые используются в качестве тестовых данных.
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        # Если встречаем фикстуру которая начинается на data_ (в тесте это переменная которая например имеет
        # имя data_groups)
        if fixture.startswith("data_"):
            # Тогда загружаем модуль который имеет такое же имя как фикстура только обрезаем первые 5 символов
            testdata = load_from_module(fixture[5:])
            # используем загруженные тестовые данные, что бы параметризовать тестовую функцию
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            # Тогда загружаем модуль который имеет такое же имя как фикстура только обрезаем первые 5 символов
            testdata = load_from_json(fixture[5:])
            # используем загруженные тестовые данные, что бы параметризовать тестовую функцию
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


# Загружаем данные из модуля с заданным именем
def load_from_module(module):
    # импортируем модул по пути указанному в скобках (путем склейки) и берет из него данные из переменной testdata
    return importlib.import_module("data.%s" % module).constant


# Функция для загрузки данных из файла json
def load_from_json(file):
    # Открываем файл с данными и передаем их в перемменную
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        # Читаем данные из открытого файла и перекодируем их в набор данных в виде объектов
        return jsonpickle.decode(f.read())


# Создаем фикстуру для работы с БД
@pytest.fixture(scope="session")
def db(request):
    # Загружаем данные из конфига из блока web
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture