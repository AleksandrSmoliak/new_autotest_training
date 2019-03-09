from fiture.application import Application
import pytest


@pytest.fixture(scope="session")
def app(request):
    # Создаем фикстуру (объект типа Application)
    fixture = Application()
    # Разрушение фикстуры используя существующий метод заррушения фикстуры
    request.addfinalizer(fixture.destroy)
    # Возвращаем фиксуру
    return fixture
