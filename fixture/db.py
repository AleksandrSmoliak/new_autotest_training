import pymysql
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        # Тут происходит инициализация соединения с БД
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        # Отключаем кэширование в БД
        self.connection.autocommit(True)

    # Загрузка списка групп из БД
    def get_group_list(self):
        # Инициализируем список в который будем помещать объекты с выборкой из БД
        list = []
        # Создаем курсор
        cursor = self.connection.cursor()
        try:
            # Создаем запрос к бд для выборки групп из базы
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            # Проходим по всем элементам из полученной выборки и присваиваем полям переменной
            for row in cursor:
                (id, name, header, footer) = row
                # Строим новый объект. Приводим ИД к строке, что бы не было ошибок при сравнении со списком приложения
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            # Закрываем курсор
            cursor.close()
        # Возвращаем получаемый список
        return list

    # Загрузка списка контактов из БД
    def get_contact_list(self):
        # Инициализируем список в который будем помещать объекты с выборкой из БД
        list = []
        # Создаем курсор
        cursor = self.connection.cursor()
        try:
            # Создаем запрос к бд для выборки контактов из базы (отбор по полю deprecated это значение не удаленных
            #  контактов)
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            # Проходим по всем элементам из полученной выборки и присваиваем полям переменной
            for row in cursor:
                (id, firstname, lastname) = row
                # Строим новый объект. Приводим ИД к строке, что бы не было ошибок при сравнении со списком приложения
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            # Закрываем курсор
            cursor.close()
        # Возвращаем получаемый список
        return list

    def destroy(self):
        self.connection.close()