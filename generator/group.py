import random
import string
import os.path
from model.group import Group
import jsonpickle


# Генератор случайных тестовых данных
def random_string(prefix, maxlen):
    # Присваиваем переменной наборы различных символов + пробел
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    # Возвращаем строку из склеенных символов. Список будет из случайных символов и случайной длинны с ограничением на
    # значение maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Формируем 2 массива с данными. Первый пустой, а второй генерируется случайными данными, при этом генерируется
# указанное количество раз, что позволяет создать нескольео наборов с данными.
testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(5)
]

# Определяем путь до текущего файла и указываем куда необходимо сохранить файл со сгенерированными тестовыми
# данными
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/group.json")

# Открываем файл на запись (w - это режим на запись)
with open(file, "w") as f:
    # Задаем формат записи в файл (в 2 уровня)
    jsonpickle.set_encoder_options("json", indent=2)
    # Преобразуем данные в формат json и записываем эти данные в файл. Так же при приобразовании в файл записывается
    # тип объекта из которого преобразуются данные в поле py/object
    f.write(jsonpickle.encode(testdata))
