from fiture.application import Application
import pytest

fixture = None  # Задаем глобальную переменную для определения валидности фикстуры


@pytest.fixture
def app():
    global fixture  # Объявление глобальной переменной
    # Проверяем, если фикстуры нету или она не валидна, тогда создаем ее.
    if fixture is None:
        # Создаем фикстуру (объект типа Application)
        fixture = Application()
    else:
        if not fixture.is_valid():
            # Создаем фикстуру (объект типа Application)
            fixture = Application()
            # Авторизация
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


# Разрушение фикстуры используя существующий метод разрушения фикстуры, а перед этим делаем логаут из системы
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    # Возвращаем фиксуру
    return fixture
