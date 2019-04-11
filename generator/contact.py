import string
import random
from model.contact import Contact
import os.path
import jsonpickle


# Генератор случайных строковых данных
def random_string(prefix, maxlen):
    # Присваиваем переменной наборы различных символов + пробел
    symbols = string.ascii_letters + string.digits + " "
    # Возвращаем строку из склеенных символов. Список будет из случайных символов и случайной длинны с ограничением на
    # значение maxlen
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# Формируем 2 массива с данными. Первый пустой, а второй генерируется случайными данными, при этом генерируется
# указанное количество раз, что позволяет создать несколько наборов с данными.
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company_name="", company_address="",
            home_phone="", mobile_phone="", work_phone="", fax_phone="", sec_phone="", email="", email2="",
            email3="", homepage="", birthday_selected="", birthmont_selected="", byear="", home_address="")] + [
    Contact(firstname=random_string("firstname_", 10), middlename=random_string("middlename_", 10),
            lastname=random_string("lastname_", 10), nickname=random_string("nickname_", 10),
            title=random_string("title_", 10), company_name=random_string("company_name_", 10),
            company_address=random_string("company_address_", 10), home_phone=random_string("home_phone_", 10),
            mobile_phone=random_string(" mobile_phone_", 10), work_phone=random_string("work_phone_", 10),
            fax_phone=random_string("fax_phone_", 10), sec_phone=random_string("sec_phone_", 10),
            email=random_string("email_", 10), email2=random_string("email2_", 10), email3=random_string("email3_", 10),
            homepage=random_string("homepage_", 10), birthday_selected="//div[@id='content']/form/select[1]//option[12]",
            birthmont_selected="//div[@id='content']/form/select[2]//option[7]", byear="1983",
            home_address=random_string("home_address_", 10))
    for i in range(10)
    ]

# Определяем путь до текущего файла и указываем куда необходимо сохранить файл со сгенерированными тестовыми
# данными
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contact.json")

# Открываем файл на запись (w - это режим на запись)
with open(file, "w") as f:
    # Задаем формат записи в файл (в 2 уровня)
    jsonpickle.set_encoder_options("json", indent=2)
    # Преобразуем данные в формат json и записываем эти данные в файл. Так же при приобразовании в файл записывается
    # тип объекта из которого преобразуются данные в поле py/object
    f.write(jsonpickle.encode(testdata))
